import argparse
import json
import os
from pathlib import Path
from libs import view
from libs import user
from hashlib import sha256

#Checks if the manager file is empy
def is_json_empty(file_path):
    return os.path.isfile(file_path) and os.path.getsize(file_path) == 0
#How to usee command for managerFile
parser = argparse.ArgumentParser(
    prog='manager.py',
    usage='python3 {prog} create-admin --username admin --password admin',
    description='A program to manage admins.'
)

parser.add_argument('command', help='The command to execute')
parser.add_argument('--username', required=True, help='The username for the admin')
parser.add_argument('--password', required=True, help='The password for the admin')

args = parser.parse_args()

if args.username and args.password:
    manager_details = {"username": args.username, "password": sha256(args.password.encode('utf-8')).hexdigest()}
    file_path=Path('data/manager.json')
    if is_json_empty('data/manager.json') or not (file_path.exists()):
        with open('data/manager.json', 'w') as f:
            with open("data/users.json", mode='r') as feedsjson:
                try:
                    users = json.load(feedsjson)
                    for user in users:
                        if args.username == user["username"]:
                            view.duplicated_user()
                            break
                    else:
                        json.dump(manager_details, f, indent=4)                       
                except json.JSONDecodeError:
                    print("JSONDecode#Error: Could not decode the JSON file")
    else:
        print("The manager is already registered")