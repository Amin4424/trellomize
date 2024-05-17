import json
import libs.view as view
import libs.get_input as input
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
    def __init__(self, name, username, password, email):
        self.name = name
        self.username = username
        self.password = password
        self.email = email
        self.user_id = str(uuid.uuid4())
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

    @staticmethod
    def sign_in():
        while True:
            view.sign_in_username()
            username=input.get_username()
            view.sign_in_password()
            password=input.get_string()
            encoded_password = encode(password)
            if Path ("data/manager.json").exists():
                try:
                    with open("data/manager.json",mode='r') as feedsjson:
                        user = json.load(feedsjson)
                        if user.get(username) == encoded_password:
                            #TODO manager section
                            pass
                except json.JSONDecodeError:
                    pass
                    
            if Path("data/users.json").exists():
                try:
                    with open("data/users.json",mode='r') as feedsjson:
                        users = json.load(feedsjson)
                        for user in users:
                            if user['username'] == username and user['password'] == encoded_password:
                                print("u signed in")
                                break
                                #It doesn't leave the loop right now but it should call another function which is related to that section
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
            users.append(entry)
            json.dump(users, feedsjson , indent=4)
