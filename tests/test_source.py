import unittest
from app.models import News

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source('kenya','newsimage','interesting',2021,'news')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))