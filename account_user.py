class User:
    """
    Class that generates new instances of users information.
    """
    users_list = [] # Empty list

    def __init__(self, first_name, last_name, login_name , login_password):

        self.first_name = first_name
        self.last_name = last_name
        self.login_name = login_name
        self.login_password = login_password

    def save_user(self):

        '''
        save_user method saves contact objects into users_list
        '''

        User.users_list.append(self)

    def delete_user(self):

        '''
        delete_contact method deletes a saved contact from the contact_list
        '''

        User.users_list.remove(self)

    @classmethod
    def find_by_login_name(cls,login_name):
        '''
        Method that takes in a username and returns a contact that matches that number.

        Args:
            login_name: login_name to search for
        Returns :
            Account details of person that matches the username.
        '''

        for user in cls.users_list:
            if user.login_name == login_name:
                return user