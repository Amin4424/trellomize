import json
import libs.view as view
import libs.get_input as input
import libs.project as project
import libs.assignment as ag
import libs.user as us
from loguru import logger
from pathlib import Path
from rich import print as rprint
import uuid
import os
from time import sleep
from libs.get_input import rusure
"""Here is for all program menu it's possible to replace it with Graphic Interface
    Because the interface and back are independent
    rest files are back of the file like :
    assignment
    project
    manager
    user
"""
class Program :
    def main():
        os.system('cls')
        rprint("[medium_purple2]Hello , Welcome to Trellomize")
        rprint("")

        while True:
            option = ''
            try:
                rprint("1.[green]Sign in")
                rprint("2.[bright_white]Sign up")
                rprint("3.[red]Exit")
                rprint("[royal_blue1]Your choice: ")
                option = input.get_string()
                if option == '1':
                    us.User.sign_in()
                    os.system("cls")
                if option == '2':
                    us.User.sign_up()
                    os.system("cls")
                if option == '3':
                    exit()
                if option not in ['1','2','3']:
                    os.system("cls")
                    rprint("Invalid input! Please try again.")
            except:
                if option == '3':
                    exit(0)
                view.for_exit()
    def user_logging_in(username):
        view.logging_in_message(username)
        logger.add('data/logging.log')
        logger.info(username+' just logged in into his/her account')
        Program.menu_after_logging_user(username)
    def menu_after_logging_user(username):
        while True:
            view.menu_after_log()
            choice = input.get_string()
            if choice == '1':
                Program.creating_project(username)
            elif choice == '2':
                Program.delete_project(username)
                break
            elif choice == '3':
                Program.working_on_project(username)
                break
            elif choice == '4':
                os.system('cls')
                Program.main()
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
                        rprint('[yellow]Which user to you want to deactive?')
                        view.users_table(users)
                        rprint('Enter the username for [yellow]deactivating:')
                        id_to_deactive = input.get_string()
                        sure = rusure()
                        if sure:
                            for user in users:
                                if user['username'] == id_to_deactive:
                                    if user['is_active'] == True:
                                        user['is_active'] = False
                                        rprint("[yellow]Deactivating was successful!")
                                        sleep(2)
                                        with open("data/users.json",mode='w') as feedsjson:
                                            json.dump(users, feedsjson, indent=4)
                                        break
                                    else:
                                        rprint("[yellow]This user is not active!")
                                        sleep(2)
                                        break
                            else:
                                rprint('[yellow]User not found!')
                                sleep(2)
                        else:
                            pass
                except json.JSONDecodeError:
                    print("JSONDecode#Error: Could not decode the JSON file")
                    
            elif choice == '2':
                try:
                    with open("data/users.json",mode='r') as feedsjson:
                        users = json.load(feedsjson)
                        rprint('[green]Wich user to you want to active?')
                        view.users_table(users)
                        rprint('Enter the user [yellow]username[white] for [green]activating:')
                        id_to_deactive = input.get_string()
                        sure = rusure()
                        if sure:
                            for user in users:
                                if user['username'] == id_to_deactive:
                                    if user['is_active'] == False:
                                        user['is_active'] = True
                                        rprint("[green]activating was seccus full!")
                                        sleep(2)
                                        with open("data/users.json",mode='w') as feedsjson:
                                            json.dump(users, feedsjson, indent=4)
                                        break
                                    else:
                                        rprint("[yellow]This user is already active!")
                                        sleep(2)
                                        break
                            else:
                                rprint('[yellow]User not found!')
                                sleep(2)
                        else:
                            pass
                except json.JSONDecodeError:
                    print("JSONDecode#Error: Could not decode the JSON file")
                    
            elif choice == '3':
                try:
                    newdata = []
                    found = False
                    with open("data/users.json",mode='r') as feedsjson:
                        users = json.load(feedsjson)
                        rprint('[red]Wich user to you want to DELETE?')
                        view.users_table(users,deleting=True)
                        rprint('Enter the user [yellow]ID[white] for [red]DELETING:')
                        id_to_deactive = input.get_string()
                        sure = rusure()
                        if sure:
                            for user in users:
                                if user['user_id'] == id_to_deactive:
                                    found = True
                                    pass
                                else:
                                    newdata.append(user)
                        else:
                            pass
                    if found:
                        with open("data/users.json", "w") as f:
                            json.dump(newdata, f, indent=4)
                        rprint('[green]User has been succusfully [red]DELETED!!')
                        sleep(2)
                    else:
                        rprint('[red]User not found!')
                        sleep(2)
                        
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
            if Path("data/projects.json").exists():
                with open("data/projects.json", mode='r') as projects_file:
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
    def delete_project(username):
        view.get_name_of_project()
        project.Project.delete_project(username)

    def working_on_project(username):
        while True:
            view.menu_work_on_project()
            choice = input.get_string()
            if choice =='1':
                project.Project.add_member_to_project(username)
            if choice =='2':
                project.Project.remove_member_from_project(username)
            if choice =='3':
                ag.Task.add_assignment(username)
            if choice =='4':
                ag.Task.remove_assignment(username)
            if choice =='5':
                ag.Task.assign_to_member(username)
            if choice =='6':
                ag.Task.remove_assignment_from_member(username)
            if choice =='7':
                ag.Task.work_on_assignments(username)
            if choice =='8':
                ag.Task.see_all_projects(username)
            if choice =='9':
                Program.menu_after_logging_user(username)