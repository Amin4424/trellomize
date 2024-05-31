import libs.user as user
import libs.get_input as input
import libs.view as view
import json
import pathlib as Path
"""Here is a menu for manager
    To activate a user
    To deactivate a user
    To Remove a user
"""
class Manager(user.User):
    
    def __init__(self, name, username, password, email):
        super().__init__(name, username, password, email)
    def remove_user():
        view.remove_member_message()
        if Path("data/users.json").exists():
            try:
                    with open("data/users.json",mode='r') as feedsjson:
                        users = json.load(feedsjson)
                        for user in users:
                            print(user['username'])
            except json.JSONDecodeError:
                print("JSONDecode#Error: Could not decode the JSON file")