import os
from rich import print as rprint
def wrong_input():
    print("Please enter a valid input!")

def get_name():
    os.system('cls')
    print("Enter your fullname:")

def get_username():
    print("Enter your username:")

def get_password():
    print("Enter your password:")

def get_email():
    print("Enter your email:")

def alreay_exist():
    print("This username has already exist!\nPlesae enter another one:")
def invalid_email():
    print("Your email is not valid. Please try again:")
def invalid_username_password():
    print("Your username or password is not valid.Please try again.")
def sign_in_username():
    print("Please enter your username:")
def sign_in_password():
    print("Please enter your password:")
def remove_member_message():
    print("Please choose a user to remove from application :")
def logging_in_message(username):
    print("Welcome dear "+username)
def menu_after_log():
    os.system('cls')
    rprint("1.Create a project")
    rprint("2.Delete a project")
    rprint("3.Work on a project")
def menu_for_manager():
    os.system('cls')
    rprint("1.Deactive a user")
    rprint("2.active a user")
    rprint("3.delete a user")
    rprint("4.Loging out")
    
def rusure():
    print('Are you sure?(y/n)')

def get_name_of_project():
    rprint('Enter the name of the project that you want to remove')
def menu_work_on_project():
    os.system('cls')
    rprint("1.Add a user to project")
    rprint("2.Remove a user from a project")
    rprint("3.Add an assignment for project")
    rprint("4.Remove an assignment from project")
    rprint("5.Assign an assignment to a user")
    # rprint("6.Work on assignment")

def duplicated_user():
    rprint("This user has already exist!")