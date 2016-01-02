import unittest, logging

logger=logging.getLogger('app')

class TestCase(unittest.TestCase):
    # Subclasses can define fixtures which will be automatically installed.
    fixtures = None

    @classmethod
    def setUpClass(cls):
        logger.debug('TestCase setup class')
        #cls._connection = createExpensiveConnectionObject()
        if cls.fixtures:
            logger.debug('TestCase setup class -> fixtures=' + ','.join(cls.fixtures))

    @classmethod
    def tearDownClass(cls):
        logger.debug('TestCase tear down class')
        #cls._connection.destroy()

    def setUp(self):
        '''
        method run when every test method starts
        
        1) create tables by fixture names
        2) populate database with fixture json file 
        '''
        logger.debug('TestCase.setUp()')
        if self.fixtures:
            logger.debug('TestCase.setUp() -> fixtures=' + ','.join(self.fixtures))

        #TODO: add code here to populate test database with fixtures

    def tearDown(self):
        '''
        method run when every test method terminates
        1) drop tables by fixture names
        '''
        logger.debug('TestCase.tearDown()')
        if self.fixtures:
            logger.debug('TestCase.tearDown() -> fixtures=' + ','.join(self.fixtures))

        #TODO: add code here to clean test database with fixtures
