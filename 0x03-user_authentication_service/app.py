#!/usr/bin/env python3
'''
Flask - app
'''
from flask import Flask, jsonify, request, abort
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    ''' the root '''
    return jsonify('{"message": "Bienvenue"}')


@app.route('/users', methods=['POST'], strict_slashes=False)
def users() -> str:
    '''
    register for new user - POST
    '''
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": f"{email}", "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"})


@app.route('/sessions', methods=['POST'])
def login() -> str:
    '''
    loggin aas a user
    '''
    email = request.form.get('email')
    password = request.form.get('password')
    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        result = jsonify({"email": f"{email}", "message": "logged in"})
        result.set_cookie('session_id', session_id)
        return result
    abort(401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
