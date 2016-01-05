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
        Query user by id, return a user dict(unicoded)  
        '''
        db_handler = DBManager.get_connection()
        account = db_handler['user'].find_one({"_id": ObjectId(oid)})
        return account

    @staticmethod
    def get_users():
        '''
        Get all users without password field, return a list of user dicts
        '''
        db_handler = DBManager.get_connection()
        cursor = db_handler['user'].find(projection={'password':False})
        return UserDao._cursor_to_list(cursor)

    @staticmethod
    def get_public_users():
        '''
        Get all users for public display
        '''
        db_handler = DBManager.get_connection()
        cursor = db_handler['user'].find(projection=['_id','name'])
        return UserDao._cursor_to_list(cursor)

    @staticmethod
    def _cursor_to_list(cursor):
        '''
        covert a cursor to a list
        '''
        collection = []
        for item in cursor:
            collection.append(item)
        return collection
