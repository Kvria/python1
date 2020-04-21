#!/usr/bin/env python3.6
from account_details import Details

def create_details(fname,lname,phone,email,e_password,acc_type,u_name,acc_password):
    '''
    Function to create a new account detail
    '''
    new_details = Details(fname,lname,phone,email,e_password,acc_type,u_name,acc_password)
    return new_details

def save_details(Details):
    '''
    Function to save the account details
    '''
    Details.save_contact()

def del_details(Details):
    '''
    Function to delete account details
    '''
    Details.delete_contact()

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
    print("Hello Welcome to your contact list. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
            print("Use these short codes : cc - create a new contact, dc - display contacts, fc -find a contact, ex -exit the contact list ")

            short_code = input().lower()

            if short_code == 'cc':
                    print("New Contact")
                    print("-"*10)

                    print ("First name ....")
                    f_name = input()

                    print("Last name ...")
                    l_name = input()

                    print("Phone number ...")
                    p_number = input()

                    print("Email address ...")
                    e_address = input()

                    print("Email password ...")
                    e_password = input()

                    print("Account type e.g instagram, facebook ...")
                    acc_type = input()

                    print("Username ...")
                    u_name = input()

                    print("Password ...")
                    print("Would you like to c")
                    acc_password = input()


                    save_details(create_details(f_name,l_name,p_number,e_address,e_password,acc_type,u_name,acc_password)) # create and save new contact.
                    print ('\n')
                    print(f"New account details {f_name} {l_name} {acc_type} {u_name} {password} created")
                    print ('\n')

            elif short_code == 'dc':

                    if display_contacts():
                            print("Here is a list of all your contacts")
                            print('\n')

                            for contact in display_contacts():
                                    print(f"{contact.first_name} {contact.last_name} .....{contact.phone_number}")

                            print('\n')
                    else:
                            print('\n')
                            print("You dont seem to have any contacts saved yet")
                            print('\n')

            elif short_code == 'fc':

                    print("Enter the number you want to search for")

                    search_number = input()
                    if check_existing_contacts(search_number):
                            search_contact = find_contact(search_number)
                            print(f"{search_contact.first_name} {search_contact.last_name}")
                            print('-' * 20)

                            print(f"Phone number.......{search_contact.phone_number}")
                            print(f"Email address.......{search_contact.email}")
                    else:
                            print("That contact does not exist")

            elif short_code == "ex":
                    print("Bye .......")
                    break
            else:
                    print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':

    main()