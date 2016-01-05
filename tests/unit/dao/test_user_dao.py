#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging, unittest
logger=logging.getLogger('app')

from dao.user_dao import UserDao

class TestAccountDao(unittest.TestCase):
    '''
    Test Account Data Access Object
    '''
    
    def test_get_account_by_id(self):
        oid = u'56840a2db37b6c16a0ef1b6c'
        user = UserDao.get_user_by_id(oid)
        logger.debug('test_get_account_by_id type={0}'.format(type(user.name)))