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
