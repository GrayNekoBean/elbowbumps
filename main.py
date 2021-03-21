from flask import Flask, request, jsonify
from flask.wrappers import Response
from elbowbumps.twitter_scraper import getTweets
from elbowbumps.twitter_id_lookup import twitterID
from flask_cors import CORS, cross_origin
from elbowbumps import create_app, db
from json import loads

app = create_app()
cors = CORS(app)
from elbowbumps.models import UserData, UserInterestData, UserMatch

user_session_keys = {}
from elbowbumps import auth

# Updates interests for a given user
@app.route('/update_interests', methods=['POST'])
def update_interests():
    param = request.args.get('user_id', None)
    print(param)
    response = {}

    # TODO: check if user exists in database

    if (param):
        response["STATUS_CODE"] = 200
        response["MESSAGE"] = f"User {param} has been updated"
    else:
        response["STATUS_CODE"] = 500
        response["MESSAGE"] = "Please provide a user id"
    return jsonify(response)

# Adds row for interest data


@app.route('/add_interest_score', methods=['POST'])
def add_interest_score():
    param = request.args.get('user_id')
    interest = UserInterestData(1, 'Basketball', 0, 0.5)
    interest2 = UserInterestData(3, 'Basketball', 0, 0.3)
    interest3 = UserInterestData(4, 'Basketball', 0, 0.4)
    db.session.add(interest)
    db.session.add(interest2)
    db.session.add(interest3)
    db.session.commit()
    return jsonify({
        'STATUS_CODE': 200,
        'MESSAGE': 'row added successfully'
    })

@app.route('/match_info', methods=['POST'])
@cross_origin()
def match_info():
    matches = loads(request.form.get('matches'))
    print(matches)
    match_info = []
    for match in matches:
        user = UserData.query.filter_by(ud_id=match['uid_ud_id']).first()
        match_info.append(user.serialise())
    return jsonify({
        "STATUS_CODE": 200,
        'match_info': match_info
    })

@app.route('/bump', methods=['POST'])
@cross_origin()
def bump():
    user_id = request.form.get('userId')
    match_id = request.form.get('matchId')
    m1 = UserMatch.query.filter(UserMatch.um_ud_id_1==user_id).filter(UserMatch.um_ud_id_2==match_id).first()
    m2 = UserMatch.query.filter(UserMatch.um_ud_id_2==user_id).filter(UserMatch.um_ud_id_1==match_id).first()
    if m1:
        m1.um_1_matched = True
        db.session.commit()
        return jsonify({"STATUS_CODE": 200})
    else:
        m2.um_2_matched = True
        db.session.commit()
        return jsonify({"STATUS_CODE": 200})

@app.route('/get_bumps', methods=['GET'])
@cross_origin()
def get_bumps():
    user_id = request.args.get('user_id')
    matches = UserMatch.query.filter((UserMatch.um_ud_id_1 == user_id) | (UserMatch.um_ud_id_2 == user_id)).filter(UserMatch.um_1_matched == True).filter(UserMatch.um_2_matched == True).all()
    match_ids = []
    for m in matches:
        if (m.um_ud_id_1 == int(user_id)):
            match_ids.append(m.um_ud_id_2)
        else:
            match_ids.append(m.um_ud_id_1)
    return jsonify({
        'matches': match_ids
    })

@app.route('/questionnaire', methods=['POST'])
@cross_origin()
def add_questionnaire_scores():
    user_id = int(request.form.get('user_id'))
    scores = request.form
    
    for cat in scores:
        
        if cat == 'user_id':
            continue
        
        # will end up being a list, probably, when we have multiple scores instrad of one
        score = scores[cat]
        # may have to change up the numbers to fit with twitter scores
        user_interests = UserInterestData.query.filter_by(uid_id=user_id).first()
        if user_interests:
            user_interests.uid_questionnaire_score = score
            user_interests.updateScores()
            db.session.commit()
        else:
            data = UserInterestData(user_id, cat, 0, score)
            db.session.add(data)
            db.session.commit()
    return jsonify({
        "STATUS_CODE": 200,
        "Message": f"Updated userID {user_id} interest data."
    })


# updating record to fill in the questionnaire score in the database - Lily
@app.route('/social_media_info', methods=['POST'])
def add_twitter_username():
    twitter = request.args.get('twitter')
    id = request.args.get('id')
    user = UserData.query.filter_by(ud_id = id).first()
    if not user:
        return jsonify({
            "STATUS_CODE": "500",
            "Message": "Please ensure the user exists!"
        })
    if (twitter == ""):
        return jsonify({
            "STATUS_CODE": "500",
            "Message": "Please provide a twitter username"
        })
    else:
        query = f'SELECT * FROM user_data WHERE ud_twitter = \'{twitter}\';'
        results = db.engine.execute(query)
        if results.rowcount == 0:
            twitter_id = twitterID(twitter)
            if twitter_id == False:
                return jsonify ({
                    "STATUS_CODE": "500",
                    "Message": "Please provide a real twitter username"
                })
            else:
                user.ud_twitter = twitter
                user.ud_id_twitter = twitter_id
                db.session.commit()
                return jsonify({
                    "STATUS_CODE": "200",
                    "Message": "Thank you!"
                })
        else:
            return jsonify ({
            "STATUS_CODE": "500",
            "Message": "Please provide a unique twitter username"
            })


# @app.route('/register', methods=['POST'])
# @cross_origin()
# def registerUser():
#     fName = request.form.get('fName')
#     sName = request.form.get('sName')
#     phoneNum = request.form.get('phoneNum')
#     emailAdd = request.form.get('emailAdd')
#     pw = request.form.get('pw')
#     user_email_check = UserData.query.filter_by(ud_email=emailAdd).first()
#     user_phone_check = UserData.query.filter_by(ud_phone=phoneNum).first()
#     if user_email_check:
#         return jsonify({
#             "STATUS_CODE": '500',
#             "Message": f"User with email {emailAdd} already registered"
#         })
#     elif user_phone_check:
#         return jsonify({
#             "STATUS_CODE": '500',
#             "Message": f"User with phone number {phoneNum} already registered"
#         })
#     elif fName == "" or sName == "" or phoneNum == "" or pw == "" or emailAdd == "":
#         return jsonify({
#             "STATUS_CODE": '500',
#             "Message": f"Fill in all fields"
#         })

#     # User data columns: forename, surname, birthyear, email, phone, password, gender, twitter
#     newUser = UserData(fName, sName, '2000', emailAdd, phoneNum, pw, 'M', '')
#     db.session.add(newUser)
#     db.session.commit()
#     # POST Request
#     return jsonify({
#         'STATUS_CODE': '200',
#         'id': newUser.ud_id
#     })


# @app.route('/login', methods=['POST'])
# def loginUser():
#     email = request.form.get('email')
#     pw = request.form.get('pw')
#     user = UserData.query.filter_by(ud_email=email).first()
#     res: Response = jsonify({})
#     if not user or user.ud_password != pw:
#         return jsonify({
#             "STATUS_CODE": "500",
#             "Message": "Please Check email or password"
#         })
#     return jsonify({
#         "STATUS_CODE": "200",
#         "id": user.ud_id,
#         "Message": "Successfully logged in"
#     })


@app.route('/get_tweets', methods=['POST'])
def get_tweets():
    user_id = request.args.get('user_id')
    category = request.args.get('category')
    user = UserData.query.filter_by(ud_id=user_id).first()
    user_interests = UserInterestData.query.filter_by(uid_id=user_id).first()
    if not user:
        return jsonify({
            "STATUS_CODE": "500",
            "Message": "Please ensure the user exists!"
            })
    elif user.ud_twitter == "":
          return jsonify({
            "STATUS_CODE": "500",
            "Message": "Please ensure the user has a social media account registered"
            })
    elif user_interests:
        user_interests.uid_twitter_score = getTweets(user.ud_id_twitter, category)
        user_interests.updateScores()
        db.session.commit()
        return jsonify({
            "STATUS_CODE": '200',
            "Message": f"Updated userID {user_id} with new category score"
        })
    else:
        score = getTweets(user.ud_id_twitter, category)
        data = UserInterestData(user_id, category, score, 0)
        db.session.add(data)
        db.session.commit()
        return jsonify({
            'status_code': '200',
            "Message": f"Added new row for userID {user_id} with new category score"
        })

# finds nearest neighbours for a given user
@app.route('/find_matches', methods=['GET'])
@cross_origin()
def find_matches():
    param = request.args.get('user_id')
    limit = request.args.get('limit')
    query = f'select uid1.uid_ud_id, uid2.uid_ud_id, sqrt(Abs(uid1.uid_squared_weight + uid2.uid_squared_weight - (2*uid1.uid_interest_weight*uid2.uid_interest_weight))) as distance from user_interest_data uid1 , user_interest_data uid2 where uid1.uid_interest_type = uid2.uid_interest_type and uid1.uid_id <> uid2.uid_id and uid1.uid_ud_id = {param} and uid1.uid_ud_id <> uid2.uid_ud_id group by uid2.uid_ud_id, uid1.uid_ud_id, uid1.uid_squared_weight,uid2.uid_squared_weight,uid1.uid_interest_weight,uid2.uid_interest_weight order by distance limit {limit};'
    results = db.engine.execute(query)
    response = []
    for res in results:
        response.append(dict(res))
        m1 = UserMatch.query.filter_by(um_ud_id_1=param,um_ud_id_2=res.uid_ud_id).first()
        m2 = UserMatch.query.filter_by(um_ud_id_2=param,um_ud_id_1=res.uid_ud_id).first()
        if not m1 and not m2:
            newMatch = UserMatch(param, res.uid_ud_id)
            db.session.add(newMatch)
    db.session.commit()
    return jsonify({
        'STATUS_CODE': '200',
        'result': response
    })

# Gets recommendations for a given user


@app.route('/get_recs_for', methods=['GET'])
def get_recs_for():
    param = request.args.get('user_id')
    test_user = "345"
    fake_users = ["556", "223"]
    if (param == test_user):
        return jsonify({
            "recommendations": fake_users,
            "STATUS_CODE": "200"
        })
    elif (param == None):
        return jsonify({
            "STATUS_CODE": "500",
            "Message": "Please provide a user id"
        })
    else:
        return jsonify({
            "STATUS_CODE": "500",
            "Message": "Please ensure user exists in database"
        })

# Test endpoint - an example of how to make a transaction


@app.route('/test_user', methods=['POST'])
def create_test_user():
    from random import randint
    user = UserData('Faridz', 'Ibrahim', 19, f'{randint(0, 6000)}',
                    f'{randint(0, 6000)}', f'{randint(0, 6000)}', 'M', f'{randint(0, 6000)}')
    db.session.add(user)
    db.session.commit()
    return jsonify({
        'STATUS_CODE': '200',
        "Message": 'User added'
    })

# A welcome message to test our server


@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
