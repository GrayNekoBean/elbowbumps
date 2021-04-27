import uuid as UUID
import hashlib
import urllib.parse

from flask import Flask, request, jsonify, Blueprint
from flask.wrappers import Request, Response
from flask_cors import CORS, cross_origin

from elbowbumps import db, create_app

from elbowbumps.models import UserData

import requests as HttpRequest


auth = Blueprint('auth', __name__)

#TODO: For safety reasons, we'd better hash the password again at here. Still, it's not unhackable, but just for a little more safe.

user_session_keys = {}
    
def RemoveSessionCookie(res: Response, userID):
    global user_session_keys
    if userID in user_session_keys:
        user_session_keys.pop(userID)
        
    res.delete_cookie("user_id")
    res.delete_cookie("session_key")
        

def SetSessionCookie(res: Response, userID):
    global user_session_keys
    uuid_ = UUID.uuid4()
    
    if userID in user_session_keys:
        user_session_keys[userID].append(uuid_)
    else:
        user_session_keys[userID] = [uuid_]
    
    res.set_cookie("user_id", str(userID))
    res.set_cookie('session_key', uuid_.bytes)


def CheckSessionCookie(req: Request):
    if 'user_id' in req.cookies and 'session_key' in req.cookies:
        uid = req.cookies.get("user_id")
        key = req.cookies.get("session_key")
        
        if uid in user_session_keys:
            if key in user_session_keys[uid]:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
    
def check_password_hash(userpw, pw):
    if pw != '':
        if hashlib.md5(pw.encode()).hexdigest() == userpw:
            return True
    return False

@auth.route('/register', methods=['POST'])
def register():
    reg_info = request.form
    if 'fName' in reg_info and 'sName' in reg_info and 'phoneNum' in reg_info and 'emailAdd' in reg_info and 'pw' in reg_info:
        fName = reg_info.get('fName')
        sName = reg_info.get('sName')
        phoneNum = reg_info.get('phoneNum')
        emailAdd = reg_info.get('emailAdd')
        pw = hashlib.md5(reg_info['pw'].encode()).hexdigest()
        user_email_check = UserData.query.filter_by(ud_email=emailAdd).first()
        user_phone_check = UserData.query.filter_by(ud_phone=phoneNum).first()
        if user_email_check:
            return jsonify({
                "STATUS": 'EMAIL_EXISTED',
                "STATUS_CODE": '500',
                "Message": f"User with email {emailAdd} already registered"
            })
        elif user_phone_check:
            return jsonify({
                "STATUS": 'PHONE_EXISTED',
                "STATUS_CODE": '500',
                "Message": f"User with phone number {phoneNum} already registered"
            })
        elif fName == "" or sName == "" or phoneNum == "" or pw == "" or emailAdd == "":
            return jsonify({
                'STATUS': 'INVALID_DATA',
                "STATUS_CODE": '500',
                "Message": f"Fill in all fields"
            })
        elif (len(fName) > 50) or (len(sName) > 50) or (len(phoneNum) > 13) or (len(pw) > 100) or (len(emailAdd) > 50):
            return jsonify({
                'STATUS': 'INVALID_DATA',
                "STATUS_CODE": '500',
                "Message": f"There is a limited number of characters per entry box"
            })
        else:
            # User data columns: forename, surname, birthyear, email, phone, password, gender, twitter
            newUser = UserData(fName, sName, '2000', emailAdd, phoneNum, pw, 'M', '')
            db.session.add(newUser)
            db.session.commit()
            # POST Request
            return jsonify({
                'STATUS': 'SUCCESS',
                'STATUS_CODE': '200',
                'id': newUser.ud_id
            })
    else:
        return jsonify({
            'STATUS': 'INVALID_DATA',
            "STATUS_CODE": '500',
            "Message": f"Fill in all fields"
        },status = 'INVALID_DATA', status_code = 500)
            
@auth.route('/login', methods=['POST'])
def loginUser():
    status = 'SUCCESS'
    status_code = 200
    msg = ''
    userID = ''
    if request.method == 'POST':
        login_info = request.form
        if login_info != None and login_info != {}:
            if 'email' in login_info and 'pw' in login_info:
                email = login_info['email']
                pw = login_info['pw']
                user = UserData.query.filter_by(ud_email=email).first()
                if not user:
                    status = "USER_NOT_EXISTS"
                    status_code = 500
                    msg = "The user doesn't exists, please check any typo in the email or register a new account"
                elif not check_password_hash(user.ud_password, pw):
                    status = "INCORRECT_PASSWORD"
                    status_code = 500
                    msg = "Incorrect password, please check any typo in the password or try go to \"forget password\""
                else:
                    userID = user.ud_id;
            else:
                status = "INVALID_DATA"
                status_code = 500
    response: Response = jsonify({'STATUS': status, "STATUS_CODE": status_code, "Message": msg, "id": userID  })
    if (status == 'SUCCESS'):
        SetSessionCookie(response, userID)
    return response

def getGravatarImage(email):
    # import code for encoding urls and generating md5 hashes
    
    # Set your variables here
    default = 'retro'
    size = 256
    
    # construct the url
    gravatar_url = "https://www.gravatar.com/avatar/" + hashlib.md5(email.lower().encode()).hexdigest() + "?"
    gravatar_url += urllib.parse.urlencode({'d':default, 's':str(size)})
    return gravatar_url

@auth.route('/twitter_timeline', methods=['GET'])
@cross_origin()
def getTwitterTimeline():
    if request.args.get('twitter'):
        twitter = request.args.get('twitter')
        response = HttpRequest.get(f'https://publish.twitter.com/oembed?url=https://twitter.com/{twitter}')
        if response.ok:
            return response.json()
    return jsonify({
        "STATUS": "SUCCESS",
        "STATUS_CODE": "200",
        "Message": "failed to call Twitter API"
    })

@auth.route('/user_data', methods=['GET', 'POST'])
#@cross_origin
def getUserData():
    if request.method == 'GET': 
        if ('user_id' in request.args):
            userId = request.args['user_id']
            userRow = UserData.query.filter_by(ud_id=userId).first()
            
            avatar = getGravatarImage(userRow.ud_email)
            fName = userRow.ud_forename
            sName = userRow.ud_surname
            email = userRow.ud_email
            phone = userRow.ud_phone
            twitter = userRow.ud_twitter
            twitter_id = userRow.ud_id_twitter
            intro = userRow.ud_intro
            bio = userRow.ud_bio
            
            return jsonify({
                "STATUS": "SUCCESS",
                "STATUS_CODE": "200",
                "data":{
                    "avatar": avatar,
                    "fName": fName,
                    "sName": sName,
                    "email": email,
                    "phone": phone,
                    "twitter": twitter,
                    "twitterID": twitter_id,
                    "intro": intro,
                    "bio": bio
                }
            })
        else:
            return jsonify({
                "STATUS": "NO_USER_ID",
                "STATUS_CODE": "403",
                "Message": "No user ID provided."
            })
    elif request.method == 'POST':
        fName = request.form.get('fName')
        sName = request.form.get('sName')
        phoneNum = request.form.get('phoneNum')
        emailAdd = request.form.get('emailAdd')
        id = request.form.get('id')
        intro = request.form.get('intro')
        bio = request.form.get('bio')

        user_email_check = UserData.query.filter_by(ud_email=emailAdd).first()
        user_phone_check = UserData.query.filter_by(ud_phone=phoneNum).first() 
        user = UserData.query.filter_by(ud_id = id).first()


        if not user:
            print(id)
            return jsonify({
                "STATUS_CODE": "500",
                "Message": "You don't seem to exist. Oops."
            })

        if user_email_check and user.ud_email != emailAdd:
            return jsonify({
                "STATUS": 'EMAIL_EXISTED',
                "STATUS_CODE": '500',
                "Message": f"User with email {emailAdd} already registered"
            })
        elif user_phone_check and user.ud_phone != phoneNum :
            return jsonify({
                "STATUS": 'PHONE_EXISTED',
                "STATUS_CODE": '500',
                "Message": f"User with phone number {phoneNum} already registered"
            })
        elif fName == "" or sName == "" or phoneNum == ""  or emailAdd == "":
            return jsonify({
                'STATUS': 'INVALID_DATA',
                "STATUS_CODE": '500',
                "Message": f"Can't leave fields blank"
            })
        elif (len(fName) > 50) or (len(sName) > 50) or (len(phoneNum) > 13) or (len(emailAdd) > 50) or (len(bio) > 2000) or (len(intro) > 160):
            return jsonify({
                'STATUS': 'INVALID_DATA',
                "STATUS_CODE": '500',
                "Message": f"There is a limited number of characters per entry box"
            })
        else:
            user.ud_email = emailAdd
            user.ud_forename = fName
            user.ud_phone = phoneNum
            user.ud_surname = sName
            user.ud_bio = bio
            user.ud_intro = intro
            db.session.commit()
            # POST Request
            return jsonify({
                'STATUS': 'SUCCESS',
                'STATUS_CODE': '200',
                'id': user.ud_id
            })
    else:
        return jsonify({
            'STATUS': 'INVALID_DATA',
            "STATUS_CODE": '500',
            "Message": f"Fill in all fields"
        },status = 'INVALID_DATA', status_code = 500)

    return jsonify({
        "STATUS": "SUCCESS",
        "STATUS_CODE": 200
    })
