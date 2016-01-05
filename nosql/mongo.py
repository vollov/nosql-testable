#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import settings as app_settings
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

class DBManager():
    '''
    Manage the database connections
    
    Encoding: MongoDB stores data in BSON format. BSON strings are UTF-8 encoded
    Unicode strings (<type 'unicode'>) are encoded UTF-8 first.
    
    query alway return a unicode dict
    '''
    
    #class level instance, gloable shared instances
    db = None
    
    @classmethod
    def init_connections(cls):
        db_host = app_settings.DB_HOST
        db_port = app_settings.DB_PORT
        db_name = app_settings.DB_NAME
        
        try:
            client = MongoClient(db_host, db_port)
            cls.db = client[db_name]
        except ConnectionFailure, e:
            sys.stderr.write("Could not connect to server: %s" % e)
            sys.exit(1)
            
    @classmethod
    def get_connection(cls):
        ''' initial db if it is None'''
        
        if not cls.db:
            cls.init_connections()
        
        return cls.db
        
