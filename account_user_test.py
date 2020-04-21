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
        self.new_user.save_user() # saving the new users details
        self.assertEqual(len(User.users_list),1)  

    def test_save_multiple_users(self):
        '''
        test_save_multiple_details to check if we can save multiple details
        objects to our details_list
        '''
        self.new_user.save_user()
        test_user = User("Test","user","login-name","login-password") # new users details
        test_user.save_user()
        self.assertEqual(len(User.users_list),2)

    def test_delete_user(self):
        '''
        test_delete_user to test if we can remove details from our users list
        '''
        self.new_user.save_user()
        test_user = User("Test","user","login-name","login-password") # new users details
        test_user.save_user()

    def test_find_details_by_login_name(self):
        '''
        test to check if we can find a details by any login_name and display information
        '''

        self.new_user.save_user()
        test_user = User("Test","user","login-name","login-password") 
        test_user.save_user()

        found_user = User.find_by_login_name("login-name") 
       
        self.assertEqual(found_user.first_name,test_user.first_name)
    

if __name__ == '__main__':
    unittest.main()