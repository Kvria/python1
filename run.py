#!/usr/bin/env python3.6
from account_details import Details
import random

def create_details(fname,lname,login_name,login_password, email,acc_type,u_name,acc_password):
    '''
    Function to create a new account detail
    '''
    new_details = Details(fname,lname,login_name,login_password, email,acc_type,u_name,acc_password)
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

def main():
        print("Hello, Welcome to PASSWORD LOCKER!")
        print("Kindly log in.")
        print('\n')
        print ("First name ....")
        f_name = input()

        print("Last name ...")
        l_name = input()

        print("Login username...")
        login_name = input()

        print("Login password...")
        login_password = input()

        while True:
                print("Welcome.....")
                print("Use these short codes : cc - create a new account details, dc - display account details, fc -find a account details, ex -exit the account details list ")

                short_code = input().lower()

                if short_code == 'cc':
                        print("Email address...")
                        email = input()

                        print("Account type e.g instagram, facebook ...")
                        acc_type = input()

                        print("Username ...")
                        u_name = input()

                        print("Password ...")
                        print("Would you like to fill in your own password or be created for?")

                        print("Use these short codes: cn - create new password, cf - created for")
                        
                        short_code = input().lower()

                        if short_code == 'cf':
                                acc_password = acc_password.randint(100000000-9999999999)
                                print(acc_password)

                        elif short_code == 'cn':
                                acc_password = input()


                        save_details( create_details(f_name,l_name,login_name,email,login_password,acc_type,u_name,acc_password)) # create and save new account details.
                        print ('\n')
                        print(f"New account details {f_name} {l_name} {acc_type}  {u_name} {acc_password} created")
                        print ('\n')

                elif short_code == 'dc':

                        if display_details():
                                print("Here is a list of all your account details")
                                print('\n')

                                for Details in display_details():
                                        print(f"{Details.first_name} {Details.last_name} {Details.acc_type} {Details.u_name} {Details.acc_password}")

                                print('\n')
                        else:
                                print('\n')
                                print("You dont seem to have any account details saved yet")
                                print('\n')

                elif short_code == 'fc':

                        print("Enter the username you want to search for")

                        search_username = input()
                        if check_existing_details(search_username):
                                search_details = find_details(search_username)
                                print(f"{search_details.first_name} {search_details.last_name}")
                                print('-' * 20)

                                print(f"Account type.......{search_details.acc_type}")
                                print(f"Username.......{search_details.u_name}")
                                print(f"Password.......{search_details.acc_password}")
                        else:
                                print("That contact does not exist")

                elif short_code == "ex":
                        print("Have a nice day .......")
                        break
                else:
                        print("I really didn't get that. Please use the short codes")

                break 

if __name__ == '__main__':

    main()