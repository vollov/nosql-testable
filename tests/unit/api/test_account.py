import logging, unittest
logger=logging.getLogger('app')

from utils.testcases import TestCase
import server_8000, json

class TestAccount(TestCase):
    '''
    Test account api with flask server
    '''
    fixtures = ['auth.json', 'store.json']
    
    def setUp(self):
        '''method run when every test method starts'''
        super(TestAccount, self).setUp()
        logger.debug('TestAccount.setUp()')
        self.app = server_8000.app.test_client()
        
# 
#     def tearDown(self):
#         ''' method run when every test method terminates'''
#         super.tearDown(self)
#         logger.debug('TestAccount.tearDown()')
        
    def test_account_list(self):
        return_view = self.app.get('/api/v1.0/account')
        actual_json = json.loads(return_view.data)
        expected_view = '''
        {
  "accounts": [
    {
      "_id": "56840a2db37b6c16a0ef1b6a", 
      "address": "55 king st, n2p 2e3", 
      "name": "dave", 
      "phone": "416-113-2345"
    }, 
    {
      "_id": "56840a2db37b6c16a0ef1b6b", 
      "address": "66 king st, n2p 2e3", 
      "name": "martin", 
      "phone": "416-223-1678"
    }, 
    {
      "_id": "56840a2db37b6c16a0ef1b6c", 
      "address": "77 king st, n2p 2e3", 
      "name": "anna", 
      "phone": "519-223-2345"
    }
  ]
}
        '''
        expected_json=json.loads(expected_view)
        self.assertEquals(actual_json,expected_json,'account list view should be equal')
        #logger.debug('TestAccount run test case 1 return_view.data={0}'.format(return_view.data))

    def test_account_lookup(self):
        return_view = self.app.get('/api/v1.0/account/56840a2db37b6c16a0ef1b6b')
        actual_json = json.loads(return_view.data)
        expected_view = '''
        {
  "account": {
    "_id": "56840a2db37b6c16a0ef1b6b", 
    "address": "66 king st, n2p 2e3", 
    "name": "martin", 
    "phone": "416-223-1678"
  }
}
        '''
        expected_json=json.loads(expected_view)
        self.assertEquals(actual_json,expected_json,'account lookup view should be equal')
        