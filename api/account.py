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

accounts = [
{ 'id': '1', "name" : "dave", "phone" : "416-113-2345", "address" : "55 king st, n2p 2e3"},
{ 'id': '2', "name" : "martin", "phone" : "416-223-1678", "address" : "66 king st, n2p 2e3"},
{ 'id': '3', "name" : "anna", "phone" : "519-223-2345", "address" : "77 king st, n2p 2e3"}
]

from flask import Blueprint, jsonify, abort

account_api = Blueprint('account_api', __name__)

@account_api.route('/api/v1.0/accounts/<oid>', methods=['GET'])
def get_account(oid):
    account = [account for account in accounts if account['id'] == oid]
    if len(account) == 0:
        abort(404)
    return jsonify({'account': account[0]})

@account_api.route('/api/v1.0/accounts', methods=['GET'])
def get_accounts():
    return jsonify({'accounts': accounts})