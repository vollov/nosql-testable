import logging, unittest
logger=logging.getLogger('app')

from tools.fixture import Fixture

class TestFixture(unittest.TestCase):
    '''
    Test data fixture tool
    '''
    
    def setUp(self):
        '''method run when every test method starts'''
        logger.debug('TestFixture.setUp()')
        self.fixture = Fixture()

    def tearDown(self):
        ''' method run when every test method terminates'''
        pass
    
    def test__parse_file_name(self):
        collection_name = self.fixture._parse_file_name('user.json')
        expected_collection_name = 'user'
        self.assertEquals(collection_name,expected_collection_name,'parse_file_name should return ' + expected_collection_name)
    
