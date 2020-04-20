class Details:
    """
    Class that generates new instances of account details.
    """
    details_list = [] # Empty list

    def __init__(self, first_name, last_name, number, email,email_password,account_name,username,password):

        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = number
        self.email = email
        self.email_password = email_password
        self.account_name = account_name
        self.username = username
        self.password = password
        
    def save_details(self):

        '''
        save_details method saves contact objects into details_list
        '''

        Details.details_list.append(self)

    def delete_details(self):

        '''
        delete_contact method deletes a saved contact from the contact_list
        '''

        Details.details_list.remove(self)

    @classmethod
    def find_by_username(cls,username):
        '''
        Method that takes in a username and returns a contact that matches that number.

        Args:
            username: username to search for
        Returns :
            Account details of person that matches the username.
        '''

        for details in cls.details_list:
            if details.username == username:
                return details

    @classmethod
    def details_exist(cls,username):
        '''
        Method that checks if a contact exists from the contact list.
        Args:
            username: username to search if it exists
        Returns :
            Boolean: True or false depending if the contact exists
        '''
        for details in cls.details_list:
            if details.username == username:
                    return True

        return False

    @classmethod
    def display_details(cls):
        '''
        method that returns the contact list
        '''
        return cls.details_list

    

        
