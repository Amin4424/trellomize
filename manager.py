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

parser = argparse.ArgumentParser(
    prog='manager.py',
    description='A program to create an admin.'
)

subparsers = parser.add_subparsers(dest='command', required=True)

# Create admin command
create_admin_parser = subparsers.add_parser('create-admin', help='Create an admin')
create_admin_parser.add_argument('--username', required=True, help='The username for the admin')
create_admin_parser.add_argument('--password', required=True, help='The password for the admin')

# Purge data command
purge_data_parser = subparsers.add_parser('purge-data', help='Clear all data')

args = parser.parse_args()
if args.command == 'create-admin':
    manager_details = {"username": args.username, "password": args.password}

    manager_file_path = "data/manager.json"

    if Path(manager_file_path).exists():
        try:
            with open(manager_file_path, mode='r') as manager_file:
                manager = json.load(manager_file)
                print("Manager already exists")
        except json.JSONDecodeError:
            manager = {}
            manager["username"] = args.username
            manager["password"] = user.hash_password_with_salt(args.password)
    else:
        manager = {}
        manager["username"] = args.username
        manager["password"] = user.hash_password_with_salt(args.password)



    with open(manager_file_path, mode='w') as manager_file:
        json.dump(manager, manager_file, indent=4)
script_dir = os.path.dirname(os.path.abspath(__file__))
if args.command == 'purge-data':
    print("Are you sure you want to delete all datas? [Y/n]")
    choice = input()
    if choice in ['y', 'yes']:
        files_to_delete = [
            "data/assignments.json",
            "data/projects.json",
            "data/users.json",
            "data/logging.log",
            "data/logfile.log",
            "data/manager.json"
        ]
        # Clears all datas in data folder
        for file_path in files_to_delete:
            abs_file_path = os.path.join(script_dir, file_path)
            if Path(abs_file_path).exists():
                os.remove(abs_file_path)
                print(f"Deleted {file_path}")

        print("All data files deleted.")
    else:
        print("Data deletion canceled.")


