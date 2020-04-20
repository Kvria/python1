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
        self.new_details = Details("Sonic","Hedgehog","0712345678","sonic@ms.com","hhogsonic","h-hog","decibels","sonic-h","hogtheG","iamsonic","son-hog")
    
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Details.details_list = []
    
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_details.first_name,"Sonic")
        self.assertEqual(self.new_details.last_name,"Hedgehog")
        self.assertEqual(self.new_details.phone_number,"0712345678")
        self.assertEqual(self.new_details.email,"sonic@ms.com")
        self.assertEqual(self.new_details.email_password,"hhogsonic")
        self.assertEqual(self.new_details.facebook_name,"sonic-h")
        self.assertEqual(self.new_details.facebook_password,"hogtheG")
        self.assertEqual(self.new_details.twitter_name,"iamsonic")
        self.assertEqual(self.new_details.twitter_password,"son-hog")
        self.assertEqual(self.new_details.instagram_name,"h-hog")
        self.assertEqual(self.new_details.instagram_password,"decibels")