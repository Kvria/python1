import unittest # Importing the unittest module
from account_details import Details # Importing the account details
import random

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
        self.new_details = Details("sonic@mns.com","instagram","h-hog","sonic-h")
    
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Details.details_list = []
    
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_details.email,"sonic@mns.com")
        self.assertEqual(self.new_details.account_type,"instagram")
        self.assertEqual(self.new_details.username,"h-hog")
        self.assertEqual(self.new_details.acc_password,"sonic-h")
    


    def test_save_details(self):
        '''
        test_save_details test case to test if the details object is saved into
        the details list
        '''
        self.new_details.save_details() # saving the new account details
        self.assertEqual(len(Details.details_list),1)

    def test_save_multiple_details(self):
        '''
        test_save_multiple_details to check if we can save multiple details
        objects to our details_list
        '''
        self.new_details.save_details()
        test_details = Details("test@user.com","facebook","testname","password") # new account details
        test_details.save_details()
        self.assertEqual(len(Details.details_list),2)

    def test_delete_details(self):
        '''
        test_delete_details to test if we can remove details from our details list
        '''
        self.new_details.save_details()
        test_details = Details("test@user.com","facebook","testname","password") # new account details
        test_details.save_details()

        self.new_details.delete_details()# Deleting details object
        self.assertEqual(len(Details.details_list),1)
       

    def test_find_details_by_username(self):
        '''
        test to check if we can find a details by any username and display information
        '''

        self.new_details.save_details(),
        test_details = Details("test@user.com","facebook","testname","password") 
        test_details.save_details()

        found_details = Details.find_by_username("testname") 
       
        self.assertEqual(found_details.email,test_details.email)
    
    def test_details_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the account details.
        '''

        self.new_details.save_details()
        test_details = Details ("test@user.com","facebook","testname","password") # new contact
        test_details.save_details()

        details_exists = Details.details_exist("testname")

        self.assertTrue(details_exists)

    def test_display_all_details(self):
        '''
        method that returns a list of all account details saved
        '''

        self.assertEqual(Details.display_details(),Details.details_list)

    
    
if __name__ == '__main__':
    unittest.main()
    