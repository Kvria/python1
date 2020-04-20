class Details:
    """
    Class that generates new instances of account details.
    """
    details_list = [] # Empty list

    def __init__(self, first_name, last_name, number, email,email_password,facebook_name,facebook_password,twitter_name,twitter_password,instagram_name,instagram_password):

        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = number
        self.email = email
        self.email_password = email_password
        self.facebook_name = facebook_name
        self.facebook_password = facebook_password
        self.twitter_name = twitter_name
        self.twitter_password = twitter_password
        self.instagram_name = instagram_name
        self.instagram_password = instagram_password

        
