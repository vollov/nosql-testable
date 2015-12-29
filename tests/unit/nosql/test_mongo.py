
import logging, unittest
logger=logging.getLogger('app')

from nosql.mongo import DBManager

class TestDBManager(unittest.TestCase):
    '''
    Demo test to show how to use sql alchemy sessions
    '''
    
    def setUp(self):
        '''set up test db'''
        logger.debug('TestDBManager setup for each method')

    def tearDown(self):
        '''tear down test db'''
        pass