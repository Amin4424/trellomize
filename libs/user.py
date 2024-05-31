import json
import libs.view as view
import libs.get_input as input
import libs.Program as uh
from pathlib import Path
import time
import re
import uuid
import hashlib
import os
salt = "trellomize"
"""In this File all stuufs related to sign in and sign up are gathered
    Including gmail validation using regex , encoding password , saving datas
    
"""
def hash_password_with_salt(password):
    data_base_password = password + salt
    return hashlib.sha256(data_base_password.encode()).hexdigest()

def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    match= re.match(pattern,email)
    if match:
        return True
    else:
        return False

class User:
    def __init__(self, name, username, password, email, is_active=True):
        self.name = name
        self.username = username
        self.password = password
        self.email = email
        self.user_id = str(uuid.uuid4())
        self.is_active = is_active
        User.add_user_to_json(self)

    
    def sign_up():
        os.system('cls')
        view.get_name()
        name = input.get_string()
        get_username = False
        users = []
        if Path("data/users.json").exists():
            with open("data/users.json", mode='r') as feedsjson:
                    try:
                        users = json.load(feedsjson)
                        while True:
                            view.get_username()
                            username = input.get_username()
                            for user in users:
                                if username == user["username"]:
                                    break
                            else:
                                get_username = True
                                break
                            view.duplicated_user()
                    except json.JSONDecodeError:
                        users = []
        else:
            users=[]
        if not(get_username):
            view.get_username()
            username = input.get_username()
        view.get_password()
        password = hash_password_with_salt(input.get_string())
        view.get_email()
        while True:
            email=input.get_string()
            if is_valid_email(email)==False:
                view.invalid_email()
            else:
                for user in users:
                    if email == user["email"]:
                        view.duplicated_email()
                        break
                else:
                    break
        new_user = User(name, username, password, email)
        view.success_sign_up()

    
    def sign_in():
        view.sign_in_username()
        username=input.get_username()
        view.sign_in_password()
        flag_2 = False
        flag_1 = False
        password = hash_password_with_salt(input.get_string())
        if Path ("data/manager.json").exists():
                with open("data/manager.json",mode='r') as feedsjson:
                    try:
                        users = json.load(feedsjson)
                        if users['username']==username and users['password']==password :
                            uh.Program.manager_logging_in(username)
                    except:
                        users=[]
                        flag_1 = True
        if Path("data/users.json").exists():
                with open("data/users.json",mode='r') as feedsjson:
                    try:
                        users = json.load(feedsjson)
                        for user in users:
                            if user['username'] ==username:
                                if not user['is_active']:
                                    os.system('cls')
                                    print("Your account is deactived by the manager")
                                    time.sleep(3)
                                elif user['username'] == username and user['password'] ==password:
                                    uh.Program.user_logging_in(username)
                                elif user['username'] == username and user['password'] != password:
                                    view.invalid_username_password()
                        
                    except json.JSONDecodeError:
                        flag_2 = True
        if flag_1 and flag_2:
            os.system('cls')
            print("There's no registered member with that username and password")
            time.sleep(3)
            
        else:
            print("User File doesn't exist")    
    
    def add_user_to_json(user):
        users = []
        if Path("data/users.json").exists():
            with open("data/users.json", mode='r') as feedsjson:
                try:
                    users = json.load(feedsjson)
                except json.JSONDecodeError:
                    users = []
        else:
            users = []
        with open("data/users.json", mode='w') as feedsjson:
            entry = {}
            entry['name'] = user.name
            entry['username'] = user.username
            entry['password'] = user.password
            entry['email'] = user.email
            entry['user_id'] = user.user_id
            entry['is_active'] = user.is_active
            users.append(entry)
            json.dump(users, feedsjson , indent=4)
    
    