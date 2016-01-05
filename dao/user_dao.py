#!/usr/bin/python
# -*- coding: utf-8 -*-

from nosql.mongo import DBManager
from bson import ObjectId

class UserDao():
    '''
    fetch the data from DB and encoded to unicode
    '''
    
    @staticmethod
    def get_user_by_id(oid):
        '''
        Query user by id 
        '''
        db_handler = DBManager.get_connection()
        account = db_handler['user'].find_one({"_id": ObjectId(oid)})
        return account