import json
import libs.view as view
import libs.get_input as input
import libs.userhandling as uh
from pathlib import Path
from rich import print as rprint
import re
import uuid
import time
import os
from datetime import datetime
#datetime.now().strftime("%Y:%m:%d:%H:%M:%S")
class Project:
    def __init__(self,name,title,leadername,ID,list_of_members):
        self.leadername=leadername
        self.name = name
        self.title = title
        self.ID=ID
        self.list_of_members=list_of_members
        # self.assignment_id = assignment_id
        # self.description = description
        # self.start_point = start_point
        # self.deadline = deadline
    def create_project(leadername,name,title,ID):
        list_of_members=[]
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
    def delete_project(username):
        if Path("data/projects.json").exists():
            with open("data/projects.json", mode='r') as existing_projects:
                datas = json.load(existing_projects)
                for i in range(len(datas)):
                    rprint(str(i+1) +f". {datas[i]['name']}")
                name_of_project=input.get_string()
                if len(datas) != 0:
                    for item in datas:
                        if item['name'] == name_of_project and item['leader'] == username:
                            rprint(f"Are you sure you want to delete {name_of_project} project?")
                            rprint("Enter [Y/n]")
                            choice = input.get_string()
                            if choice.lower() in ['y', 'yes']:
                                datas.remove(item)
                                rprint("The project successfuly deleted")
                                time.sleep(3)
                                with open("data/projects.json", mode='w') as updated_projects:
                                    json.dump(datas, updated_projects, indent=4)
                                uh.Program.menu_after_logging_user(username)
                            else:
                                uh.Program.menu_after_logging_user(username)
                        elif item['name'] == name_of_project and item['leader'] != username:
                            rprint("You cannot remove the project because you are not the leader.")
                            time.sleep(3)
                            uh.Program.menu_after_logging_user(username)
                        elif item['name'] != name_of_project:
                            uh.Program.menu_after_logging_user(username)
                            time.sleep(3)
                            rprint("The name you provided does not exist in projects.")
                else:
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
            except json.JSONDecodeError:
                print("JSONDecodeError: Could not decode the JSON file")
                time.sleep(3)
                uh.Program.menu_after_logging_user(username)
    def remove_member_to_project(username):
        if Path("data/users.json").exists():
                try:
                    with open("data/projects.json", mode='r') as projects_file:
                        projects = json.load(projects_file)
                        while True:
                            is_empty = False
                            rprint("Select a project :")
                            for project in projects:
                                if project['leader'] == username:
                                    rprint(project)
                            name_of_project=input.get_string()
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
                                    if name_to_remove in temp:
                                        temp.remove(name_to_remove)
                                        project['list_of_members'] = temp  # Assign the updated list back to the project
                                        with open("data/projects.json", mode='w') as updated_projects_file:
                                            json.dump(projects, updated_projects_file, indent=4)
                                        is_deleted = True
                                        os.system('cls')
                                        rprint("The member was successfully deleted from the project.")
                                        time.sleep(3)
                                        uh.Program.menu_after_logging_user(username)
                                        break
                            else:
                                rprint("The name is not valid")
                                time.sleep(3)
                                os.system('cls')

                except json.JSONDecodeError:
                    print("JSONDecodeError: Could not decode the JSON file")
                    time.sleep(3)
                    uh.Program.menu_after_logging_user(username)