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
        #logger.debug('test_get_account_by_id type={0}'.format(type(user['name'])))
        expected_user_name = u'anna'
        self.assertEquals(user['name'],expected_user_name,'signed user name should be {0}'.format(expected_user_name))

    def test_get_users(self):
        users = UserDao.get_users()
        logger.debug('test_get_users size={0}'.format(type(users)))
        expected_size = 3
        self.assertEquals(len(users),expected_size,'number of users should be {0}'.format(expected_size))
