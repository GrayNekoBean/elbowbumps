from flask import Flask, request, jsonify
from flask.wrappers import Response
from __main__ import app

#TODO: For safety reasons, we'd better hash the password again at here. Still, it's not unhackable, but just for a little more safe.

@app.route('/register', methods=('GET', 'POST'))
def register():
    response = 'SUCCESS'
    reg_info = request.get_json()
    if request.method == 'POST':
        #TODO: register new accound
        print('username: ', reg_info['fName'] + reg_info['sName'])
        print('email: ', reg_info['emailAdd'])
        print('phone number: ', reg_info['phoneNum'])
        print('hashed password: ', reg_info['pw'])
        print('register')
    return jsonify({"status": response})

@app.route('/login', methods=('GET', 'POST'))
def login():
    response = "SUCCESS"
    login_info = request.get_json()
    if request.method == 'POST':
        #TODO: login to an exiting accound
        print('email: ', login_info['email'])
        print('hashed password: ', login_info['password'])
        print('login')
    return jsonify({'status': response})