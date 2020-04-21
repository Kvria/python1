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
                    print("Would you like to fill in your own password or be created for?")

                    while True:
                        print("Use these short codes: cn - create new password, cf - created for")
                        
                        short_code = input().lower()

                        if short_code == 'cn':
                            acc_password = random.randint(0,999999999)
                            print(acc_password)

                        elif short_code == input().lower()
                            acc_password = input()

                        else:
                            print("I really didn't get that. Please use the short codes")

                    save_details(create_details(f_name,l_name,p_number,e_address,e_password,acc_type,u_name,acc_password)) # create and save new contact.
                    print ('\n')
                    print(f"New account details {f_name} {l_name} {acc_type} {u_name} {acc_password} created")
                    print ('\n')

            elif short_code == 'dc':

                    if display_details():
                            print("Here is a list of all your account details")
                            print('\n')

                            for Details in display_details():
                                    print(f"{details.first_name} {details.last_name} {details.acc_type} {details.u_name} {details.acc_password}")

                            print('\n')
                    else:
                            print('\n')
                            print("You dont seem to have any account details saved yet")
                            print('\n')

            elif short_code == 'fc':

                    print("Enter the username you want to search for")

                    search_username = input()
                    if check_existing_details(search_details):
                            search_details = find_details(search_details)
                            print(f"{search_details.first_name} {search_details.last_name}")
                            print('-' * 20)

                            print(f"Phone number.......{search_details.phone_number}")
                            print(f"Email address.......{search_details.email}")
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

if __name__ == '__main__':

    main()