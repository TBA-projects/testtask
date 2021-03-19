#! /usr/bin/python3

import requests
import gitlab
import os

gl = gitlab.Gitlab('http://192.168.1.87', 'G48XGZ7LG8_TcNM24tf1')

### FUNCTIONS ###

def display_title_bar():
    # Clears the terminal screen, and displays a title bar.
    os.system('clear')

    print("\t**********************************************")
    print("\t***         Create user for gitlab         ***")
    print("\t**********************************************")

def get_user_choice():
    # Let users know what they can do.
    print("\n[1] Create new user.")
    print("[2] List users")
    print("[3] Delete user by id")
    print("[q] Quit.")

    return input("What would you like to do? ")

def add_new_user():
# user_data = {'email': 'john@doe.com','password': 's3cur3s3cr3T','username': 'jdoe','name': 'John Doe'}
    try:
        email = input("\n Entre email address: ")
        passwd = input("\n Entre user password: ")
        username = input("\n Entre username: ")
        name  = input("\n Entre name: ")
        confirm = True

        user_data = {'email': email,'password': passwd,'username': username,'name': name, 'skip_confirmation': confirm}
        user = gl.users.create(user_data)
    except Exception as e:
        print(e)

def show_user_list():
    try:
        users = gl.users.list()
        #print(users)
        #user = gl.users.get(2)
        #print(user)
        
        for user in users:
            print(str(user.id), str(user.name), str(user.email))

    except Exception as e:
        print(e)

def delete_user():
    try:
        user_id = input("\n Entre user id for delete")
        gl.users.delete(user_id)
    except Exception as e:
        print(e)


def quit():
    try:
        print("\n Thanks for using")
    except Exception as e:
        print("\n Thanks for using")
        print(e)

### MAIN PROGRAM ###

# Set up a loop where users can choose what they'd like to do.
# names = load_names()

choice = ''
display_title_bar()
while choice != 'q':

    choice = get_user_choice()

    # Respond to the user's choice.
    display_title_bar()
    if choice == '1':
        add_new_user()
    elif choice == '2':
        show_user_list()
    elif choice == '3':
        delete_user()
    elif choice == 'q':
        quit()
        print("\nBye. Bye.")
    else:
        print("\nI didn't understand that choice.\n")


# users = gl.users.list()
# print(users)
# response = requests.get("http://192.168.1.87/api/v4/projects")
# print(response)
# user_data = {'email': 'john@doe.com','password': 's3cur3s3cr3T','username': 'jdoe','name': 'John Doe'}
# user = gl.users.create(user_data)
