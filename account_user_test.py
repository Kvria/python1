import unittest # Importing the unittest module
from account_user import User # Importing the users information.

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the users class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Sonic","Hedgehog","hhogtheG","sonicunder")

     def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.users_list = []

    def test_save_user(self):
        '''
        test_save_users test case to test if the details object is saved into
        the users list
        '''
        self.new_user.test_save_user() # saving the new users details
        self.assertEqual(len(User.users_list),1)  

if __name__ == '__main__':
    unittest.main()