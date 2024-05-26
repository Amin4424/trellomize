import json
import libs.view as view
import libs.get_input as input
import libs.userhandling as uh
from pathlib import Path
import re
import uuid
from hashlib import sha256

salt = "trlumiz"

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

    @staticmethod
    def sign_up():
        view.get_name()
        name = input.get_string()
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
                            break
                        view.duplicated_user()
                except json.JSONDecodeError:
                    print("JSONDecode#Error: Could not decode the JSON file")
        view.get_password()
        password = sha256(input.get_string().encode('utf-8')).hexdigest()
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
            password = sha256(input.get_string().encode('utf-8')).hexdigest()
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
                            if user['username'] == username and user['password'] == password:
                                uh.Program.user_logging_in(username)
                            elif user['username'] == username and user['password'] != password+salt:
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
            entry['password'] = user.password
            entry['email'] = user.email
            entry['user_id'] = user.user_id
            entry['is_active'] = user.is_active
            users.append(entry)
            json.dump(users, feedsjson , indent=4)
    
    