#!/usr/bin/env python3.6
from account_details import Details
from account_user import User
import random

def create_user(first_name,last_name,login_name,login_password):
    '''
    Function to create a new user details
    '''
    new_user = User(first_name,last_name,login_name,login_password)
    return new_user

def save_user(User):
    '''
    Function to save the users details
    '''
    User.save_user()

def find_user(login_name):
    '''
    Function that finds user by login_name and returns the users details
    '''
    return User.find_by_login_name(login_name)

def check_existing_user(login_name):
    '''
    Function that check if users details exist with that  login username and return a Boolean
    '''
    return User.user_exists(login_name)

def create_details(email,acc_type,u_name,acc_password):
    '''
    Function to create a new account detail
    '''
    new_details = Details( email,acc_type,u_name,acc_password)
    return new_details

def save_details(Details):
    '''
    Function to save the account details
    '''
    Details.save_details()

def del_details(Details):
    '''
    Function to delete account details      
    '''
    Details.delete_details()

def find_details(username):
    '''
    Function that finds account details by username and returns the account details
    '''
    return Details.find_by_username(username)

def check_existing_details(username):
    '''
    Function that check if account details exist with that username and return a Boolean
    '''
    return Details.details_exist(username)

def display_details():
    '''
    Function that returns all the saved account details
    '''
    return Details.display_details()

def create_acc_password():
    acc_password = ""
    num = "0123456789"
    letters = "abecdefghijklmnopqrstuvwxyz"
        
    for x in range(4):
        acc_password += random.choice(num) + random.choice(letters)

    return acc_password

def main():
        print("Hello, Welcome to PASSWORD LOCKER!")

        while True:
                print("What do you want to do? Use these short codes: li - log in, su - sign up")

                short_code = input().lower()

                if short_code == 'su':
                        print('\n')
                        print ("First name ....")
                        f_name = input()

                        print("Last name ...")
                        l_name = input()

                        print("Login username...")
                        login_name = input()

                        print("Login password...")
                        login_password = input()

                        save_user(create_user(f_name,l_name,login_name,login_password))

                        print("Account created!")

                elif short_code == 'li':

                        print("Login username...")
                        login_name = input()

                        print("Login password...")
                        login_password = input() 

                        if check_existing_user(login_name):
                                print("Welcome.....")
                                while True:
 
                                 print("Use these short codes : cc - create a new account details, dd - display account details, fd -find a account details, dl - delete account details,ex -exit the account details list ")
                                 short_code = input().lower()
                        

                                 if short_code == 'cc':
                                        print("Email address...")
                                        email = input()

                                        print("Account type e.g instagram, facebook ...")
                                        acc_type = input()

                                        print("Username ...")
                                        u_name = input()

                                        print("Password ...")
                                        print("Would you like to fill in your own password or be created for one?")

                                        while True:

                                           print("Use these short codes: cn - create new password, cf - created for")
                                           short_code = input().lower()
                                        
                                           if short_code == 'cf':
                                                acc_password = create_acc_password()
                                                print(acc_password)
                                                break

                                           elif short_code == 'cn':
                                                acc_password = input()

                                                break
                                        save_details(create_details(email,acc_type,u_name,acc_password)) # create and save new account details.
                                        print ('\n')
                                        print(f"New account details {acc_type}  {u_name} {acc_password} created")
                                        print ('\n')

                                 elif short_code == 'dd':

                                        if display_details():
                                                print("Here is a list of all your account details")
                                                print('\n')

                                                for Details in display_details():
                                                        print(f" {Details.account_type} {Details.username} {Details.acc_password}")

                                                print('\n')
                                        
                                        else:
                                                print('\n')
                                                print("You dont seem to have any account details saved yet")
                                                print('\n')

                                 elif short_code == 'fd':

                                        print("Enter the username you want to search for")
 
                                        search_username = input()
                                        if check_existing_details(search_username):
                                                search_details = find_details(search_username)
                                                print(f"{search_details.email} ")
                                                print('-' * 20)

                                                print(f"Account type.......{search_details.account_type}")
                                                print(f"Username.......{search_details.username}")
                                                print(f"Password.......{search_details.acc_password}")
                                        else:
                                                print("That credential does not exist")
                                                

                                 elif short_code == 'dl':
                                        print("Which account details do you want to delete?") 
                                        search_username = input()    
                                        if check_existing_details(search_username):
                                           search_details = find_details(search_username)
                                           del_details(search_details)
                                           print("Account details has been deleted.")

                                        else:
                                           print("There are no account details to delete.")

                                 elif short_code == "ex":
                                        print("Have a nice day .......")
                                        break
                                 else:
                                        print("I really didn't get that. Please use the short codes")

                                

if __name__ == '__main__':

    main()