import json
import libs.view as view
import libs.get_input as input
import libs.Program as uh
import libs.save_user_action as log
from pathlib import Path
from rich import print as rprint
import re
import uuid
import time
import os
""" Here is for making project
    Adding a user to project
    Remove project
    Removing a user from project
    It has some prints and inputs here
    But it could be deleted for GUI purpose
"""
class Project:
    def __init__(self,name,title,leadername,ID,list_of_members):
        self.leadername=leadername
        self.name = name
        self.title = title
        self.ID=ID
        self.list_of_members=list_of_members
    def create_project(leadername,name,title,ID):
        list_of_members=[leadername]
        project = Project(leadername,name,title,ID,list_of_members)
        if Path("data/projects.json").exists():
            with open("data/projects.json", mode='r') as projects:
                try:
                    datas = json.load(projects)
                except json.JSONDecodeError:
                    datas = []
        else:
            datas = []
        with open("data/projects.json",mode='w') as projects:
            data = {
            'leader': leadername,
            'name': name,
            'title': title,
            'ID': ID,
            'list_of_members': list_of_members
        }
            datas.append(data)
            json.dump(datas, projects, indent=4)
        log.announcement.info(leadername + " created a project.")
        os.system('cls')
        rprint("Project has been successfully created")
        time.sleep(3)
        uh.Program.menu_after_logging_user(leadername)
    def delete_project(username):
        os.system('cls')
        if Path("data/projects.json").exists():
            with open("data/projects.json", mode='r') as existing_projects:
                try: 
                    projects = json.load(existing_projects)
                except json.JSONDecodeError:
                    rprint("Project file is empty.")
                    time.sleep(3)
                    uh.Program.menu_after_logging_user(username)
                get_name = False
                while not (get_name):
                    os.system('cls')
                    rprint("Choose your project to delete .")
                    counter =0
                    for project in projects:
                        if project['leader'] == username:
                            counter+=1
                            rprint(str(counter) + '. name: ' + project['name'] + " ID : " + project['ID'])
                    if counter ==0:
                        os.system('cls')
                        rprint("You don't have any projects to delete")
                        time.sleep(2)
                        uh.Program.menu_after_logging_user(username)
                    choice = input.get_string()
                    counter = 0
                    for project in projects:
                        if project['leader'] == username:
                            counter+=1
                            if str(counter) == choice:
                                target_project = project
                                get_name = True
                                break
                    else:
                        rprint("Please enter a valid input")
                        time.sleep(2)
                rprint(f"Are you sure you want to delete {target_project['name']} project?")
                rprint("Enter [Y/n]")
                choice = input.get_string()
                if choice.lower() in ['y', 'yes']:
                    projects.remove(target_project)
                    with open("data/assignments.json", mode='r') as assignments:
                        try:
                            tasks = json.load(assignments)
                        except json.JSONDecodeError:
                            tasks = []
                    filtered_tasks = [task for task in tasks if task['id_of_project'] != target_project['ID']]
                    with open("data/assignments.json" , mode= 'w') as updated_tasks:
                        json.dump(filtered_tasks , updated_tasks , indent= 4)
                    with open("data/projects.json", mode='w') as updated_projects:
                        json.dump(projects, updated_projects, indent=4)
                    log.announcement.info(username + " deleted the " + target_project['name'] + " project.")
                    print("The project successfuly deleted")
                    time.sleep(3)
                    uh.Program.menu_after_logging_user(username)
                else:
                    uh.Program.menu_after_logging_user(username)
                
    def add_member_to_project(username):
        if Path("data/projects.json").exists() and Path("data/users.json").exists():
            with open("data/projects.json" , mode= 'r') as file:
                try:
                    counter = 0
                    projects = json.load(file)
                    for project in projects:
                                if project['leader'] == username:
                                    counter += 1
                    if counter == 0:
                        os.system('cls')
                        rprint("[red]You don't have any projects")
                        time.sleep(3)
                        uh.Program.menu_after_logging_user(username)
                except:
                    os.system('cls')
                    rprint("Project file is empty")
                    time.sleep(3)
                    uh.Program.menu_after_logging_user(username)
        else :
            os.system('cls')
            rprint("The file of projects or users is missing")
            time.sleep(3)
            uh.Program.menu_after_logging_user(username)
            
        os.system('cls')
        with open("data/users.json", mode='r') as feedsjson:
            try:
                users = json.load(feedsjson)
            except FileNotFoundError:
                rprint("There is no user to add to your project.")
                time.sleep(3)
                uh.Program.menu_after_logging_user()
            get_name = False
            while not (get_name):
                counter = 0
                rprint("[medium_violet_red]Enter your choice to add the user to the project:")
                for user in users:
                    if user['username'] != username:
                        counter += 1
                        rprint(str(counter) + ".[light_salmon3] " + user['username'])
                if counter == 0:
                    os.system('cls')
                    rprint("There is no user to add to the project")
                    time.sleep(2)
                    uh.Program.menu_after_logging_user(username)
                choice = input.get_string()
                counter =0
                for user in users:
                    if user['username'] != username:
                        counter += 1
                        if str(counter) == choice:
                            member = user['username']
                            get_name = True
                            break
                else:
                    os.system('cls')
                    rprint("Enter a valid input")
                    time.sleep(3)
        
        rprint(f"[pale_green1]Choose from your projects to add {member} to a project:")
        with open("data/projects.json", mode='r') as projects_file:
            projects = json.load(projects_file)
            get_project = False
            while not(get_project):
                counter = 0
                for project in projects:
                    if project['leader'] == username:
                        counter += 1
                        rprint(str(counter) + ". " + project['name'])
                choice = input.get_string()
                counter =0
                for project in projects:
                    if project['leader'] == username:
                        counter +=1
                        if str(counter) == choice:
                            name_of_project = project['name']
                            get_project = True 
                            break
                else:
                    os.system('cls')
                    rprint("Please enter a valid input")
                    time.sleep(2)
            with open("data/projects.json", mode='r') as projects_file:
                projects = json.load(projects_file)
                for project in projects:
                    if project['name'] == name_of_project:
                        temp = project['list_of_members']
                        if str(member) in temp:
                            os.system('cls')
                            rprint("The user already exists in the project")
                            time.sleep(3)
                            uh.Program.menu_after_logging_user(username)
                        temp.append(str(member))
            with open("data/projects.json", mode='w') as updated_projects_file:
                json.dump(projects, updated_projects_file, indent=4)
            os.system('cls')
            rprint("User has successfuly added to project")
            time.sleep(3)
            uh.Program.menu_after_logging_user(username)
    def remove_member_from_project(username):
        if Path("data/users.json").exists():
            with open("data/projects.json", mode='r') as projects_file:
                try:
                    projects = json.load(projects_file)
                except json.JSONDecodeError:
                    os.system('cls')
                    print("You don't have any projects")
                    time.sleep(3)
                    uh.Program.menu_after_logging_user(username)
            while True:
                os.system('cls')
                counter =0
                is_empty = False
                rprint("Select a project :")
                for project in projects:
                    if project['leader'] == username:
                        counter+=1
                        rprint(str(counter) + '- ')
                        view.print_project_table(project)
                if counter == 0:
                    os.system('cls')
                    rprint("You don't have any projects")
                    time.sleep(3)
                    uh.Program.menu_after_logging_user(username)
                choice = input.get_string()
                if (choice.isdigit()) and int(choice) in range(1, counter + 1):
                    counter = 0
                    for project in projects:
                        if project['leader'] == username:
                            counter+=1
                            if str(counter) == choice:
                                name_of_project = project['name']
                for project in projects:
                    if project['name'] == name_of_project:
                        if len(project['list_of_members']) == 0:
                            rprint("This project has no member")
                            is_empty=True
                if any(name_of_project == project['name'] for project in projects) and not(is_empty):
                    break
                print("Please choose a valid project")
                time.sleep(3)
                os.system('cls')
            is_deleted=False
            while not is_deleted:
                rprint("Enter the name of the member that you want to be deleted from project")
                name_to_remove=input.get_string()
                for project in projects:
                    if project['name'] == name_of_project:
                        temp = project['list_of_members']
                        if name_to_remove == project['leader']:
                            os.system('cls')
                            rprint("You cannot delete yourself as a member from your project")
                            time.sleep(3)
                            uh.Program.menu_after_logging_user(username)
                        if name_to_remove in temp:
                            temp.remove(name_to_remove)
                            project['list_of_members'] = temp 
                            with open("data/assignments.json" , mode='w+') as assignments:
                                try:
                                    tasks = json.load(assignments)
                                    for task in tasks:
                                        if task['name_of_project'] == project:
                                            temp = task['assignees']
                                            temp.remove(name_to_remove)
                                except:
                                    tasks={}
                                json.dump(tasks , assignments , indent=4)
                            with open("data/projects.json", mode='w') as updated_projects_file:
                                json.dump(projects, updated_projects_file, indent=4)
                            is_deleted = True
                            log.announcement.info(username + " removed " + name_to_remove + " from" + name_of_project + " project.")
                            os.system('cls')
                            rprint("The member was successfully deleted from the project.")
                            time.sleep(3)
                            uh.Program.menu_after_logging_user(username)
                else:
                    rprint("The name is not valid")
                    time.sleep(3)
                    os.system('cls')
                    uh.Program.menu_after_logging_user(username)
                