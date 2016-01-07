# -*- coding: utf-8 -*-
#!/usr/bin/python

'''
account json API

GET        api/v1.0/account              - Retrieve list of account
GET        api/v1.0/account/[oid]        - Retrieve a account
POST       api/v1.0/account              - Create a new account
PUT        api/v1.0/account/[oid]        - Update an existing account
DELETE     api/v1.0/account/[oid]        - Delete a account
'''

from flask import Blueprint, jsonify, abort, json,make_response 
from nosql.mongo import DBManager
from bson import ObjectId
from utils.json_util import JsonUtil,JSONEncoder

from dao.user_dao import UserDao

account_api = Blueprint('account_api', __name__)

def get_account_by_name(name):
    pass

@account_api.route('/api/v1.0/account/<oid>', methods=['GET'])
def get_account(oid):
    db_handler = DBManager.get_connection()
    account = db_handler['user'].find_one({"_id": ObjectId(oid)})
    
    if not account:
        abort(404)
    
    account = JsonUtil.itemToStr(account)
    return jsonify({'account': account})

@account_api.route('/api/v1.0/account', methods=['GET'])
def get_accounts():
    #db_handler = DBManager.get_connection()
    #cursor = db_handler['user'].find(projection={'password':False})
    
    #accounts = JsonUtil.listToStr(cursor)
    accounts = UserDao.get_users();
    #accounts = json.dumps(cursor)
    json_resp = jsonify({'accounts': JSONEncoder().encode(accounts)})
    
    res = make_response(json_resp, 200)
    res.headers['Content-Type'] = 'text/json; charset=utf-8'
    return res

@account_api.route('/api/v1.0/public/account', methods=['GET'])
def get_public_accounts():
    #db_handler = DBManager.get_connection()
    #cursor = db_handler['user'].find(projection=['_id','name'])

    #accounts = JsonUtil.listToStr(cursor)
    accounts = UserDao.get_users();
    #accounts = json.dumps(cursor)
    return jsonify({'accounts': accounts})
