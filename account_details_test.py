import unittest # Importing the unittest module
from account_details import Details # Importing the account details

class TestDetails(unittest.TestCase):

    '''
    Test class that defines test cases for the details class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_contact = Details("Sonic","Hedgehog","0712345678","sonic@ms.com","hhogsonic","h-hog","decibels","sonic-h","hogtheG","iamsonic","son-hog")