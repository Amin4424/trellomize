import json
import libs.view as view
import libs.get_input as input
import libs.project as project
from loguru import logger
from pathlib import Path
from rich import print as rprint
import uuid
import os
class Program :
    @staticmethod
    def create_project():
        pass #TODO
    def remove_project():
        pass #TODO
    @staticmethod
    def user_logging_in(username):
        view.logging_in_message(username)
        logger.add('data/logging.log')
        logger.info(username+' just logged in into his/her account')
        Program.menu_after_logging_user(username)
    def menu_after_logging_user(username):
        view.menu_after_log()
        choice = input.get_string()
        while True:
            if choice == '1':
                Program.creating_project(username)
            elif choice == '2':
                break
            elif choice == '3':
                break
            else:
                print("Invalid input.")
    def manager_logging_in(username):
        view.logging_in_message(username)
        logger.add('data/logging.log')
        logger.info(username+ ' just logged into his/her account')
        view.menu_for_manager()
        choice = input.get_string()
        while choice!='4':
            if choice == '1':
                try:
                    with open("data/users.json",mode='r') as feedsjson:
                        users = json.load(feedsjson)
                        print('Wich user to you want to deactive?')
                        for i in range(len(users)):
                            rprint(str(i+1) + ('.') + users[i]['username'] + ' ID: ' + users[i]['user_id'])
                        print('Enter the user ID for deactivating:')
                        id_to_deactive = input.get_string()
                        view.rusure()
                        inpt = input.get_string()
                        if inpt=='y' or inpt=='Y':
                            for user in users:
                                if user['user_id'] == id_to_deactive:
                                    if user['is_active'] == True:
                                        user['is_active'] = False
                                        print("Deactivating was seccus full!")
                                        with open("data/users.json",mode='w') as feedsjson:
                                            json.dump(users, feedsjson, indent=4)
                                        break
                                    else:
                                        print("This user is not active!")
                                        break
                            else:
                                print('User not found!')
                        elif inpt=='n' or inpt=='N':
                            pass
                except json.JSONDecodeError:
                    print("JSONDecode#Error: Could not decode the JSON file")
                    
            elif choice == '2':
                try:
                    with open("data/users.json",mode='r') as feedsjson:
                        users = json.load(feedsjson)
                        print('Wich user to you want to active?')
                        for i in range(len(users)):
                            rprint(str(i+1) + ('.') + users[i]['username'] + ' ID: ' + users[i]['user_id'])
                        print('Enter the user ID for activating:')
                        id_to_deactive = input.get_string()
                        view.rusure()
                        inpt = input.get_string()
                        if inpt=='y' or inpt=='Y':
                            for user in users:
                                if user['user_id'] == id_to_deactive:
                                    if user['is_active'] == False:
                                        user['is_active'] = True
                                        print("activating was seccus full!")
                                        with open("data/users.json",mode='w') as feedsjson:
                                            json.dump(users, feedsjson, indent=4)
                                        break
                                    else:
                                        print("This user is already active!")
                                        break
                            else:
                                print('User not found!')
                        elif inpt=='n' or inpt=='N':
                            pass
                except json.JSONDecodeError:
                    print("JSONDecode#Error: Could not decode the JSON file")
                    
            elif choice == '3':
                try:
                    with open("data/users.json",mode='r') as feedsjson:
                        users = json.load(feedsjson)
                        print('Wich user to you want to DELETE?')
                        for i in range(len(users)):
                            rprint(str(i+1) + ('.') + users[i]['username'] + ' ID: ' + users[i]['user_id'])
                        print('Enter the user ID for DELETING:')
                        id_to_deactive = input.get_string()
                        view.rusure()
                        inpt = input.get_string()
                        if inpt=='y' or inpt=='Y':
                            for user in users:
                                if user['user_id'] == id_to_deactive:
                                    # TODO deleting user
                                    break
                            else:
                                print('User not found!')
                        elif inpt=='n' or inpt=='N':
                            pass
                except json.JSONDecodeError:
                    print("JSONDecode#Error: Could not decode the JSON file")

            elif choice == '4':
                pass
            else:
                print("Invalid input.")
            view.menu_for_manager()
            choice = input.get_string()

    def menu_after_logging_manager():
        view.menu_for_manager()
    def creating_project(username):
        os.system('cls')
        print('Enter name of the project')
        project_name = input.get_string()
        print('Enter a title for your project')
        project_title = input.get_string()

        while True:
            print('Enter an ID for your project')
            project_ID = input.get_string()
            if Path("data/project.json").exists():
                with open("data/project.json", mode='r') as projects_file:
                    try:
                        existing_projects = json.load(projects_file)
                        for existing_project in existing_projects:
                            if existing_project['ID'] == project_ID:
                                print("Enter another ID. The ID you entered already exists.")
                                break
                        else:
                            break  
                    except json.JSONDecodeError:
                        existing_projects = []
                        break
            else:
                break  

        project.Project.create_project(username, project_name, project_title, project_ID)
    
                        
        