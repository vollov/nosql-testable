# -*- coding: utf-8 -*-
#!/usr/bin/python

'''
authentication utility APIs
'''

from flask import Blueprint, jsonify, abort
from flask.ext.httpauth import HTTPBasicAuth


auth = HTTPBasicAuth()
auth_api = Blueprint('account_api', __name__)


def get_token():
    pass

def generate_auth_token():
    return 'auth_dummy_token'


def verify_auth_token(token):
    '''
    if token is correct, return user
    '''
    pass


@app.route('/api/resource')
@auth.login_required
def get_resource():
    return jsonify({ 'data': 'Hello, %s!' % g.user.username })

@auth.verify_password
def verify_password(username_or_token, password):
    # first try to authenticate by token
    user = User.verify_auth_token(username_or_token)
    if not user:
        # try to authenticate with username/password
        user = User.query.filter_by(username = username_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True
