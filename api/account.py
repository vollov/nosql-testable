# -*- coding: utf-8 -*-

from flask import Blueprint, Response, request
from flask.ext.restful import Resource

class AccountApi(Resource):
    
    
    def get(self, oid):
        ''' 