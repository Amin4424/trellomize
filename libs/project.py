import json
import libs.view as view
import libs.get_input as input
import libs.userhandling as uh
import libs.log as log
from pathlib import Path
from rich import print as rprint
import re
import uuid
import time
import os

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
                    datas = json.load(existing_projects)
                    for i in range(len(datas)):
                        rprint(str(i+1) +f". {datas[i]['name']}")
                    name_of_project=input.get_string()
                    if any(name_of_project == data['name'] for data in datas):
                        for item in datas:
                            if item['name'] == name_of_project and item['leader'] == username:
                                rprint(f"Are you sure you want to delete {name_of_project} project?")
                                rprint("Enter [Y/n]")
                                choice = input.get_string()
                                if choice.lower() in ['y', 'yes']:
                                    datas.remove(item)
                                    with open("data/assignments.json" , mode='w+') as assignments:
                                        try:
                                            tasks = json.load(assignments)
                                            for task in tasks:
                                                if task['name_of_project'] == name_of_project:
                                                    tasks.remove(task)
                                            json.dump(tasks , assignments , indent= 4)
                                        except:
                                            tasks = []
                                    with open("data/projects.json", mode='w') as updated_projects:
                                        json.dump(datas, updated_projects, indent=4)
                                    log.announcement.info(username + " deleted the " + name_of_project + " project.")
                                    rprint("The project successfuly deleted")
                                    time.sleep(3)
                                    uh.Program.menu_after_logging_user(username)
                                else:
                                    uh.Program.menu_after_logging_user(username)
                            elif item['name'] == name_of_project and item['leader'] != username:
                                rprint("You cannot remove the project because you are not the leader.")
                                time.sleep(3)
                                uh.Program.menu_after_logging_user(username)
                    else:
                        os.system('cls')
                        rprint("The name you provided does not exist in projects.")
                        time.sleep(3)
                        uh.Program.menu_after_logging_user(username)
                except json.JSONDecodeError:
                    rprint("Project file is empty.")
                    time.sleep(3)
                    uh.Program.menu_after_logging_user(username)
    def work_on_project():
        pass
    def add_member_to_project(username):
        os.system('cls')
        rprint("Type a username to add the user to the project:")
        if Path("data/users.json").exists():
            try:
                with open("data/users.json", mode='r') as feedsjson:
                    users = json.load(feedsjson)
                    counter = 0
                    while True:
                        for user in users:
                            if user['username'] != username:
                                counter += 1
                                rprint(str(counter) + ". " + user['username'])
                        member = input.get_string()
                        if any(member == user['username'] for user in users):
                            break
                        counter =0
                        os.system('cls')
                        rprint("Enter a valid username")
            except FileNotFoundError:
                rprint("The 'data/users.json' file does not exist.")
                time.sleep(3)
                uh.Program.menu_after_logging_user()
            os.system('cls')
            rprint(f"Choose from your projects to add {member} to a project:")
            with open("data/projects.json", mode='r') as projects_file:
                projects = json.load(projects_file)
                counter = 0
                while True:
                    for project in projects:
                        if project['leader'] == username:
                            counter += 1
                            rprint(str(counter) + ". " + project['name'])
                    if counter != 0:
                        name_of_project = input.get_string()
                        if any(name_of_project == project['name'] for project in projects):
                            break
                        counter=0
                    else:
                        os.system('cls')
                        time.sleep(3)
                        rprint("You don't have any projects")
                        uh.Program.menu_after_logging_user(username)

            try:
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
            except json.JSONDecodeError:
                print("JSONDecodeError: Could not decode the JSON file")
                time.sleep(3)
                uh.Program.menu_after_logging_user(username)
    def remove_member_from_project(username):
        if Path("data/users.json").exists():
                try:
                    with open("data/projects.json", mode='r') as projects_file:
                        projects = json.load(projects_file)
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
                        rprint("Enter the name of the member that you want to be deleted from project")
                        name_to_remove=input.get_string()
                        is_deleted=False
                        while not is_deleted:
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
                                                        for item in temp:
                                                            temp.remove(name_to_remove)
                                            except:
                                                tasks={}
                                        with open("data/projects.json", mode='w') as updated_projects_file:
                                            json.dump(projects, updated_projects_file, indent=4)
                                        json.dump(tasks , assignments , indent=4)
                                        is_deleted = True
                                        log.announcement.info(username + " removed " + name_to_remove + " from" + name_of_project + " project.")
                                        os.system('cls')
                                        rprint("The member was successfully deleted from the project.")
                                        time.sleep(3)
                                        uh.Program.menu_after_logging_user(username)
                                        break
                            else:
                                rprint("The name is not valid")
                                time.sleep(3)
                                os.system('cls')
                                uh.Program.menu_after_logging_user(username)
                except json.JSONDecodeError:
                    print("JSONDecodeError: Could not decode the JSON file")
                    time.sleep(3)
                    uh.Program.menu_after_logging_user(username)