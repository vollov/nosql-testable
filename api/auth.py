# -*- coding: utf-8 -*-
#!/usr/bin/python

'''
authentication utility APIs
'''

from flask import Blueprint, jsonify, abort
from flask.ext.httpauth import HTTPBasicAuth
from nosql.mongo import DBManager
import settings as app_settings

auth = HTTPBasicAuth()
auth_api = Blueprint('account_api', __name__)

# def get_token():
#     pass
# 
# def generate_auth_token():
#     return 'auth_dummy_token'
# 
# 
# def verify_auth_token(token):
#     '''
#     if token is correct, return user
#     '''
#     pass

from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)
from nosql.mongo import DBManager
from bson import ObjectId
from utils.json_util import JSONEncoder
import bcrypt, json
from flask import g


import logging
logger=logging.getLogger('app')

class Authen():
    
    @staticmethod
    def generate_auth_token(user_id, expiration = 600):
        '''
        Generate the token by sign the user id, return signed string
        '''
        signature_serializer = Serializer(app_settings.SECRET_KEY, expires_in = expiration)
        return signature_serializer.dumps({ 'id': user_id })

    @staticmethod
    def verify_auth_token(token):
        '''
        verfiy the token, and return the user object
        '''
        signature_serializer = Serializer(app_settings.SECRET_KEY)
        try:
            data = signature_serializer.loads(token)
        except SignatureExpired:
            return None # valid token, but expired
        except BadSignature:
            return None # invalid token
        user = Authen.get_user_by_id(data['id'])
        return user
    
    @staticmethod
    def get_user_by_id(id):
        '''
        Query user by id, return user dict
        '''
        db_handler = DBManager.get_connection()
        user = db_handler[app_settings.AUTH_TABLE_NAME].find_one({"_id": ObjectId(id)})
        # translate  ObjectId(id) to string id
        logger.debug('Authen.get_user_by_id()={0}'.format(type(user)))
        return user
    
    @staticmethod
    def set_password(username, password):
        '''
        persist password string as hash into database 
        '''
        salt = bcrypt.gensalt()
        password_hash_string = bcrypt.hashpw(password, salt)
        db_handler = DBManager.get_connection()
        db_handler[app_settings.AUTH_TABLE_NAME].update({'name': username}, {'$set': {'password': password_hash_string}})

    @staticmethod
    def compare_password(db_password_hash, password):
        '''
        compare password hash
        '''
        hash = bcrypt.hashpw(password, db_password_hash)
        
        if hash == db_password_hash:
            return True
        else:
            return False
        
    @staticmethod
    def authenticate(username, password):
        '''
        verify password with username and password
        '''
        db_handler = DBManager.get_connection()
        user = db_handler[app_settings.AUTH_TABLE_NAME].find_one({'name': username})
        db_hashed_password = str(user['password'])
        logger.debug('authenticate user type={0}'.format(type(user)))
        if not user or not Authen.compare_password(db_hashed_password, password):
            return None
        else:
            return user
        
@auth_api.route('/api/resource')
@auth.login_required
def get_resource():
    return jsonify({ 'data': 'Hello, resource!' })

@auth.verify_password
def verify_password(username_or_token, password):
    '''
    call back method for @auth.login_required
    verify the request with either token or user password pair
    
    if username_or_token is token, return user
    else, query user and password pair
    '''
    user = None
    # if password is empty string, it is a token
    if not password:
        user = Authen.verify_auth_token(username_or_token)
    else:
        user = Authen.authenticate(username_or_token, password)
    if not user:
        return False
    else:
        g.user = user
        return True
