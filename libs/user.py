import json
import libs.view as view
import libs.get_input as input
import libs.userhandling as uh
from pathlib import Path
import re
import uuid

def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    match= re.match(pattern,email)
    if match:
        return True
    else:
        return False

def encode(password):
    return ''.join(format(ord(char), '02x') for char in password)

class User:
    def __init__(self, name, username, password, email, is_active=True):
        self.name = name
        self.username = username
        self.password = password
        self.email = email
        self.user_id = str(uuid.uuid4())
        self.is_active = is_active
        User.add_user_to_json(self)

    @staticmethod
    def sign_up():
        view.get_name()
        name = input.get_string()
        view.get_username()
        username = input.get_username()
        view.get_password()
        password = input.get_string()
        view.get_email()
        while True:
            email=input.get_string()
            if is_valid_email(email)==False:
                view.invalid_email()
            else:
                break
        new_user = User(name, username, password, email)
        uh.Program.user_logging_in(username)

    @staticmethod
    def sign_in():
        while True:
            view.sign_in_username()
            username=input.get_username()
            view.sign_in_password()
            password=input.get_string()
            encoded_password = encode(password)
            if Path ("data/manager.json").exists():
                    with open("data/manager.json",mode='r') as feedsjson:
                        user = json.load(feedsjson)
                        if len(user) != 0:
                            if user['username']==username and user['password']==password:
                                uh.Program.manager_logging_in(username)
                            else:
                                view.invalid_username_password()
                    
            if Path("data/users.json").exists():
                try:
                    with open("data/users.json",mode='r') as feedsjson:
                        users = json.load(feedsjson)
                        for user in users:
                            if user['username'] == username and user['password'] == encoded_password:
                                uh.Program.user_logging_in(username)
                            elif user['username'] == username and user['password'] != encoded_password:
                                view.invalid_username_password()
                            
                except json.JSONDecodeError:
                    print("JSONDecode#Error: Could not decode the JSON file")
                    
    @staticmethod
    def add_user_to_json(user):
        users = []
        if Path("data/users.json").exists():
            with open("data/users.json", mode='r') as feedsjson:
                try:
                    users = json.load(feedsjson)
                except json.JSONDecodeError:
                    users = []
        with open("data/users.json", mode='w') as feedsjson:
            entry = {}
            entry['name'] = user.name
            entry['username'] = user.username
            entry['password'] = encode(user.password)
            entry['email'] = user.email
            entry['user_id'] = user.user_id
            entry['is_active'] = user.is_active
            users.append(entry)
            json.dump(users, feedsjson , indent=4)
    
    