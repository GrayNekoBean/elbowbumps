import uuid as UUID
import hashlib

from flask import Flask, request, jsonify
from flask.wrappers import Request, Response
from __main__ import app

from elbowbumps import db

from elbowbumps.models import UserData

import requests as HttpRequest

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

@app.route('/register', methods=('GET', 'POST'))
def register():
    reg_info = request.form
    if request.method == 'POST':
        emailAdd = reg_info['emailAdd']
        if not UserData.query.filter_by(ud_email=emailAdd).first():
            fName = reg_info['fName']
            sName = reg_info['sName']
            phoneNum = reg_info['phoneNum']
            pw = hashlib.md5(reg_info['pw'].encode()).hexdigest()
            newUser = UserData(fName, sName, '2000', emailAdd, phoneNum, pw, 'M', '', '')
            db.session.add(newUser)
            db.session.commit()
            return jsonify({
                "STATUS": "SUCCESS",
                "STATUS_CODE": "200",
                'id': newUser.ud_id
            })
        else:
            return jsonify({
                "STATUS": "USER_EXISTS",
                "STATUS_CODE": "500",
                "Message": "Please Check email or password"
            })

@app.route('/login', methods=['GET', 'POST'])
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
        else:
            status = "EMPTY_DATA"
            status_code = 500
    response = jsonify({'STATUS': status, "STATUS_CODE": status_code, "Message": msg, "id": userID  })
    if (status == 'SUCCESS'):
        SetSessionCookie(response, userID)
    return response

def getImgurImage(imageHash):
    if imageHash != '':
        clientId = '7a7f16c6427fe66'
        clientKey = 'aff912158a681cfb6abcea498c90a03c8bd451ad'
        
        header = {'Authorization': f'Client-ID {clientId}'}
        
        imageInfo = HttpRequest.get(url=f"https://api.imgur.com/3/image/{imageHash}", headers=header).json()
        srcLink = imageInfo['link']
        return srcLink
    else:
        return ''

@app.route('/user_data', methods=['GET', 'POST'])
def getUserData():
    if request.method == 'GET': 
        if ('user_id' in request.args):
            userId = request.args['user_id']
            userRow = UserData.query.filter_by(ud_id=userId).first()
            
            avatar = getImgurImage(userRow.ud_avatar)
            fName = userRow.ud_forename
            sName = userRow.ud_surname
            email = userRow.ud_email
            phone = userRow.ud_phone
            twitter_id = userRow.ud_id_twitter
            
            return jsonify({
                "STATUS": "SUCCESS",
                "STATUS_CODE": "200",
                "data":{
                    "avatar": avatar,
                    "fName": fName,
                    "sName": sName,
                    "email": email,
                    "phone": phone,
                    "twitter": twitter_id
                }
            })
        else:
            return jsonify({
                "STATUS": "NO_USER_ID",
                "STATUS_CODE": "403",
                "Message": "No user ID provided."
            })
    elif request.method == 'POST':
        
        #TODO: Update user data according to the data given in the request. If someone can do it I will be very glad.  お願いします。
        return jsonify({
            "STATUS": "SUCCESS",
            "STATUS_CODE": 200
        })
        
