import argparse
import json
import os
from pathlib import Path
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
    manager_details = {"username": args.username, "password": args.password}
    with open('manager.json', 'w') as f:
        file_path=Path('manager.json')
        if is_json_empty('manager.json') or not (file_path.exists()):
            json.dump(manager_details, f, indent=4)
        else:
            print("The manager is already registered")

