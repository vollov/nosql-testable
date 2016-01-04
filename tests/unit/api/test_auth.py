import logging, unittest
logger=logging.getLogger('app')

from utils.testcases import TestCase
import server_8000, json

from api.auth import Authen

class TestAuthen(unittest.TestCase):
    '''
    Test Authen class
    '''
    
    def test_generate_auth_token(self):
        uid = '56840a2db37b6c16a0ef1b6a'
        signed = Authen.generate_auth_token(uid)
        logger.debug('TestAuthen test_generate_auth_token signed=' + signed)
    
    def test_verify_auth_token(self):
        uid = '56840a2db37b6c16a0ef1b6a'
        token = Authen.generate_auth_token(uid)
        
        user = Authen.verify_auth_token(token)
        expected_user_name = 'dave'
        self.assertEquals(user['name'],expected_user_name,'signed user name should be {0}'.format(expected_user_name))
        
    def test_get_user_by_id(self):
        uid = '56840a2db37b6c16a0ef1b6b'
        user = Authen.get_user_by_id(uid)
        expected_user_name = 'martin'
        #logger.debug('test_get_user_by_id() user_name = ' + user['name'])
        self.assertEquals(user['name'],expected_user_name,'user name should be {0} for id {1}'.format(expected_user_name, uid))
        
    def test_authenticate(self):
        name = 'martin'
        password = '$2b$12$g4N.QUH073SqNZ2REt822uPOgvpmBGF318SnAwGL0fSq76fstJX2a'
        expected_phone = '416-223-1678'
        user = Authen.authenticate(name, password)
        logger.debug('test_authenticate() user = {0}'.format(type(user)))
        for k, v in user.iteritems():
            logger.debug('test_authenticate() user = {0},{1}'.format(k, v))

        #self.assertEquals(user['phone'], expected_phone, 'user phone should be {0}'.format(expected_phone))
