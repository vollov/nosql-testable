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
    