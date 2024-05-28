import json
import libs.view as view
import libs.userhandling as uh
import libs.log as log
from pathlib import Path
from rich import print as rprint
import re
import uuid
import time
import os
from enum import Enum
from datetime import datetime , timedelta
class Task:
    def __init__(self , title , description , start_point , deadline , project,
                 specific_id , assignees , priority , status , comment
                 ) :
        self.title = title
        self.description = description
        self.start_point = start_point
        self.deadline = deadline
        self.project = project
        self.specific_id = specific_id
        self.assignees = assignees
        self.priority = priority
        self.status = status
        self.comment = comment
    def add_assignment(username):
        with open("data/projects.json" , mode='r') as project_json:
            projects=json.load(project_json)
            while True:
                counter =0
                os.system('cls')
                rprint("Choose your project to add assignment")

                for project in projects:
                    if project['leader'] == username:
                        counter+=1
                        rprint(str(counter) + '. ' +  project['name'])
                if counter ==0:
                        os.system('cls')
                        print("You don't have any project . First make a project")
                        time.sleep(3)
                        uh.Program.menu_after_logging_user(username)        
                name_of_project = input('Enter your choice (name of the project) : ')
                if any (name_of_project == project['name'] for project in projects):
                    break
                else :
                    os.system('cls')
                    rprint('Please enter a valid name')
                    time.sleep(3)
            topic = input("Enter a topic for the assignment : ")
            description = input("Enter a description for the assignment : ")
            while True:
                os.system('cls')
                print("Choose the priority for the task")
                rprint("1.CRITICAL")
                rprint("2.HIGH")
                rprint("3.MEDIUM")
                rprint("4.LOW")
                priority = input()
                if priority == '1' or priority.lower() == "critical":
                    priority == PriorityType.CRITICAL
                    break
                if priority == '2' or priority.lower() == "high":
                    priority == PriorityType.HIGH
                    break
                if priority == '3' or priority.lower() == "medium":
                    priority == PriorityType.MEDIUM
                    break
                if priority == '4' or priority.lower() == "low":
                    priority == PriorityType.LOW
                    break
                else:
                    os.system('cls')
                    rprint("Please enter a valid priority")
                    time.sleep(3)
            starting_point = datetime.now()
            deadline = starting_point + timedelta (hours= 24)
            starting_point_str = starting_point.strftime("%Y-%m-%d %H:%M")
            deadline_str = deadline.strftime("%Y-%m-%d %H:%M")
            id = str(uuid.uuid4())
            message = username +" created a task."
            new_assignment = Task(topic ,description ,starting_point , deadline ,name_of_project ,
                                      id , [] ,priority , StatusType.BACKLOG , {} )
            if Path("data/assignments.json").exists():
                with open("data/assignments.json" , mode='r') as feedsjson:
                    try:
                        datas = json.load(feedsjson)
                    except json.JSONDecodeError:
                        datas = []
            else:
                datas =[]
            data = {
                'topic' : topic,
                'description' : description,
                'starting_point' : str(starting_point),
                'deadline' : str(deadline),
                'name_of_project' : name_of_project,
                'id' : id,
                'assignees' : [],
                'priority' : priority,
                'status' : StatusType.BACKLOG.name,
                'comments' : {}
            }
            datas.append(data)
            log.announcement.info(username + " added a task to "  + " project.")
            with open("data/assignments.json" , mode='w') as task:
                json.dump(datas , task , indent=4)
            uh.Program.menu_after_logging_user(username)
    def remove_assignment(username):
        if Path("data/projects.json").exists():
            with open("data/projects.json", mode='r') as feedsjson:
                try:
                    projects = json.load(feedsjson)
                    while True:
                        os.system('cls')
                        counter=0
                        for project in projects:
                            if project['leader'] ==username:
                                counter+=1
                                rprint(str(counter) + '. ' + project['name'])
                        name_of_project = input('Enter the name of the project : ')
                        if any (name_of_project == project['name'] for project in projects):
                            break
                        else:
                            os.system('cls')
                            rprint("Please enter a valid name .")
                            time.sleep(3)
                except json.JSONDecodeError:
                    os.system('cls')
                    print("Failed to open the projects file")
                    time.sleep(3)
                    uh.Program.menu_after_logging_user(username)
        else:
            rprint("File not found")
            time.sleep(3)
            uh.Program.menu_after_logging_user(username)
        if Path("data/assignments.json").exists():
            with open("data/assignments.json" , mode='r') as feeds:
                try:
                    tasks = json.load(feeds)
                    while True:
                        os.system('cls')
                        counter=0
                        for task in tasks:
                            if task['name_of_project'] == name_of_project:
                                counter+=1
                                rprint(str(counter) + '. ' + task['topic'])
                        topic_name = input('Choose the task to be removed  ')
                        if any (topic_name == task['topic'] for task in tasks):
                            tasks.remove(task)
                            log.announcement.info(username + " removed a task from " + task['name_of_project'] + " project.")
                            with open("data/assignments.json" , mode='w') as updated_file:
                                json.dump(tasks , updated_file , indent=4)
                            os.system('cls')
                            rprint("The task successfuly has been removed")
                            time.sleep(3)                                
                            uh.Program.menu_after_logging_user(username)
                        else:
                            os.system('cls')
                            rprint("Please enter a valid name .")
                            time.sleep(3)
                except json.JSONDecodeError:
                    os.system('cls')
                    print("Failed to open the projects file")
                    time.sleep(3)
                    uh.Program.menu_after_logging_user(username)
        else:
            rprint("File not found")
            time.sleep(3)
            uh.Program.menu_after_logging_user(username)
    def assign_to_member(username):
        if Path("data/projects.json").exists():
            with open("data/projects.json" , mode='r') as feeds:
                try:
                    projects = json.load(feeds)
                    while True:
                        counter = 0
                        os.system('cls')
                        for project in projects :
                            if project['leader'] == username:
                                counter +=1
                                rprint(str(counter) + '. ' +project['name'])
                        name_of_project = input('Enter the name of the project : ')
                        if any ((name_of_project == project['name'] and len(project['list_of_members']) != 0 ) for project in projects):
                            while True:
                                for project in projects:
                                    if project['name'] == name_of_project:
                                        for item in project['list_of_members']:
                                            print(item)
                                member_name = input("Enter the member name to add assignment to him/her : ")
                                if any(member_name in project['list_of_members'] for project in projects):
                                    break
                            break
                        if any ((name_of_project == project['name'] and len(project['list_of_members']) == 0 ) for project in projects):
                            rprint("This project has no member . please choose another one")
                            time.sleep(3)
                        else:
                            os.system('cls')
                            rprint("Please enter a valid name .")
                            time.sleep(3)
                except json.JSONDecodeError:
                    os.system('cls')
                    print("Failed to open the projects file")
                    time.sleep(3)
                    uh.Program.menu_after_logging_user(username)
        else:
            rprint("File not found")
            time.sleep(3)
            uh.Program.menu_after_logging_user(username)
        if Path("data/assignments.json").exists():
            with open("data/assignments.json" , mode='r') as feeds:
                try:
                    tasks = json.load(feeds)
                    while True:
                        os.system('cls')
                        counter=0
                        while True:
                            counter=0
                            for task in tasks:
                                if task['name_of_project'] == name_of_project:
                                    counter+=1
                                    rprint(str(counter) + '. ' + task['topic'] +" ID :" + task['id'])
                            if counter == 0:
                                os.system('cls')
                                rprint("The project you selected has no task to do")
                                time.sleep(3)
                                uh.Program.menu_after_logging_user(username)
                            choice = input('Enter your choice (num) : ')
                            if (choice.isdigit()) or int(choice) in range(1, counter + 1):
                                counter=0
                                for task in tasks:
                                    if task['name_of_project'] == name_of_project:
                                        counter+=1
                                        if choice == str(counter):
                                            list_of_members = task['assignees']
                                            if member_name in list_of_members:
                                                os.system('cls')
                                                print("User already has that task")
                                                time.sleep(3)
                                                uh.Program.menu_after_logging_user(username)
                                            log.announcement.info(username + " assigned a task to " + member_name)
                                            list_of_members.append(str(member_name))
                                            with open("data/assignments.json" , mode ='w') as updated_file:
                                                json.dump(tasks , updated_file , indent=4)
                                os.system('cls')
                                rprint("Task has been assigned .")
                                time.sleep(3)                                
                                uh.Program.menu_after_logging_user(username)
                            else:
                                os.system('cls')
                                rprint("Please enter a valid input .")
                                time.sleep(3)
                except json.JSONDecodeError:
                    os.system('cls')
                    print("The assignment file is empty")
                    time.sleep(3)
                    uh.Program.menu_after_logging_user(username)
        else:
            rprint("File not found")
            time.sleep(3)
            uh.Program.menu_after_logging_user(username)
    
    def remove_assignment_from_member(username):
        if Path("data/projects.json").exists():
            with open("data/projects.json" , mode='r') as feeds:
                try:
                    projects = json.load(feeds)
                    while True:
                        os.system('cls')
                        counter=0
                        for project in projects:
                            if project['leader'] == username:
                                counter+=1
                                rprint(str(counter) + '. ' + project['name'])
                        name_of_project = input('Enter the name of the project : ')
                        if any (project['name'] == name_of_project for project in projects):
                            if Path("data/projects.json").exists():
                                with open("data/assignments.json" , mode='r') as task_file:
                                    tasks = json.load(task_file)
                                    while True:
                                        os.system('cls')
                                        counter = 0
                                        for task in tasks:
                                            if task['name_of_project'] == name_of_project:
                                                counter+=1
                                                rprint(str(counter) + '. name : ' + task['topic'] + ' ID :' + task['id'])
                                        choice = input('Enter your choice (num) : ')
                                        if not choice.isdigit() or int(choice) not in range(1, counter + 1):
                                            os.system('cls')
                                            rprint("Enter a valid input")
                                            time.sleep(3)
                                        else:
                                            counter=0
                                            for task in tasks:
                                                if task['name_of_project'] == name_of_project:
                                                    counter+=1
                                                    if str(counter) == str(choice):
                                                        temp = task['assignees']
                                                        while True:
                                                            counter=0
                                                            for item in temp:
                                                                counter+=1
                                                                rprint(str(counter) + '. ' + item)
                                                            member_name = str(input('Enter the name of member to remove assignment from him/her : '))
                                                            if (member_name in temp):
                                                                break
                                                            else:
                                                                os.system('cls')
                                                                rprint("Enter a valid input")
                                                                time.sleep(3)
                                                        temp.remove(member_name)
                                                        task['assignees'] = temp
                                                        log.announcement.info(username + " removed "+member_name + " from an assignment.")
                                                        with open('data/assignments.json' , mode='w') as updated_file:
                                                            json.dump(tasks , updated_file , indent= 4)
                                                        os.system('cls')
                                                        rprint("Member has been removed successfuly.")
                                                        time.sleep(3)
                                                        uh.Program.menu_after_logging_user(username)
                                            
                            else:
                                rprint("File not found")
                                time.sleep(3)
                                uh.Program.menu_after_logging_user(username)  
                except json.JSONDecodeError:
                    os.system('cls')
                    rprint("File doesn't have appropriate datas")
                    time.sleep(3)
                    uh.Program.menu_after_logging_user(username)
        else:
            rprint("File not found")
            time.sleep(3)
            uh.Program.menu_after_logging_user(username)                                            
    def work_on_assignments(username):
        os.system('cls')
        if Path("data/assignments.json").exists():
            with open("data/assignments.json" , mode='r') as assignments:
                try:
                    tasks = json.load(assignments)
                    counter=0
                    while True:
                        for task in tasks:
                            members = task['assignees']
                            if username in members:
                                counter+=1
                                rprint("name : " + str(counter) +'. ' + task['topic'] +' ID ' + task['id'] )
                        if counter == 0:
                            os.system('cls')
                            print("You don't have assignments")
                            time.sleep(3)
                            uh.Program.menu_after_logging_user(username)
                        choice = input("Enter your choice to print the datas of the project: ")
                        if not choice.isdigit() or int(choice) not in range(1, counter + 1):
                            os.system('cls')
                            rprint("Enter a valid input")
                            time.sleep(3)
                        else:
                            break
                    counter =0
                    for task in tasks:
                            members = task['assignees']
                            if username in members:
                                counter+=1
                                if str(counter) == choice:
                                    assignment = task
                                    view.print_task_table(task)
                    while True:
                        rprint("1.Change Priority")
                        rprint("2.Change Status")
                        rprint("3.Add comment")
                        rprint("4.Change description")
                        rprint("5.Exit this section")
                        choice = input('Enter your choice : ')
                        if choice == '1':
                            assignment = Task.change_priority(assignment)
                            view.print_task_table(assignment)
                            log.announcement.info(username + " changed the priority of the " + assignment['name_of_project'] + " project.")
                        if choice == '2':
                            assignment = Task.change_status(assignment)
                            view.print_task_table(assignment)
                            log.announcement.info(username + " changed the status of the " + assignment['name_of_project'] + " project.")
                        if choice == '3':
                            assignment = Task.add_comment(username  , assignment)
                            view.print_task_table(assignment)
                            log.announcement.info(username + " added a comment to " + assignment['name_of_project'] + " project.")
                        if choice == '4':
                            assignment = Task.change_description(assignment)
                            view.print_task_table(assignment)
                            log.announcement.info(username + " changed the description of the " + assignment['name_of_project'] + " project.")
                        if choice == '5':
                            break   
                        else:
                            print("Enter a valid input")
                    with open("data/assignments.json" , mode='w') as updated_file:
                        json.dump(tasks,updated_file,indent=4)
                    uh.Program.menu_after_logging_user(username)
                except json.JSONDecodeError:
                    print("File doesn't not have suitable data")
    def change_priority(assignment):
        while True:
                os.system('cls')
                print("Choose the priority for the task")
                rprint("1.CRITICAL")
                rprint("2.HIGH")
                rprint("3.MEDIUM")
                rprint("4.LOW")
                priority = input()
                if priority == '1' or priority.lower() == "critical":
                    priority == PriorityType.CRITICAL
                    break
                if priority == '2' or priority.lower() == "high":
                    priority == PriorityType.HIGH
                    break
                if priority == '3' or priority.lower() == "medium":
                    priority == PriorityType.MEDIUM
                    break
                if priority == '4' or priority.lower() == "low":
                    priority == PriorityType.LOW
                    break
                else:
                    os.system('cls')
                    rprint("Please enter a valid priority")
                    time.sleep(3)
        assignment['priority'] = priority
        os.system('cls')
        rprint("Priority has been changed")
        time.sleep(3)
        return assignment
    def change_status(assignment):
        while True:
                os.system('cls')
                print("Choose the status for the task")
                rprint("1.ARCHIEVED")
                rprint("2.DONE")
                rprint("3.DOING")
                rprint("4.TODO")
                rprint("5.BACKLOG")
                status = input()
                if status == '1' or status.lower() == "archieved":
                    status == StatusType.ARCHIEVED
                    break
                if status == '2' or status.lower() == "done":
                    status == StatusType.DONE
                    break
                if  status == '3' or status.lower() == "doing":
                    status == StatusType.DOING
                    break
                if status == '4' or status.lower() == "todo":
                    status == StatusType.TODO
                    break
                if status == '5' or status.lower() == "BACKLOG":
                    status == StatusType.BACKLOG
                else:
                    os.system('cls')
                    rprint("Please enter a valid priority")
                    time.sleep(3)
        assignment['status'] = status
        os.system('cls')
        rprint("Status has been changed")
        time.sleep(3)
        return assignment
    def add_comment(username , assignment):
        os.system('cls')
        print("Type your comment to add to assignment :")
        message = str(input())
        data = {str(username): message}
        assignment['comments'].update(data)
        return assignment
    def change_description(assignment):
        os.system('cls')
        print("Enter your description to change description of the project")
        new_description = input()
        assignment['description'] = new_description
        return assignment
    def see_all_projects(username):
        os.system('cls')
        if Path("data/projects.json").exists() and Path("data/assignments.json").exists():
            with open("data/projects.json" , mode='r') as project_file:
                try:
                    projects = json.load(project_file)
                    while True:
                        counter=0
                        for project in projects :
                            if username in project['list_of_members']:
                                counter+=1
                                rprint(str(counter) + '. ' + project['name'])
                        if counter ==0:
                            os.system('cls')
                            print("You are not member of any projects")
                            time.sleep(3)
                            uh.Program.menu_after_logging_user(username)
                        choice = input('Enter your choice for project (num) : ')
                        if not choice.isdigit() or not int(choice) in range(1, counter + 1):
                            os.system('cls')
                            rprint("Enter a valid input")
                            time.sleep(3)
                        else :
                            counter =0
                            for project in projects :
                                if username in project['list_of_members']:
                                    counter+=1
                                    if str(counter) == choice:
                                        project_holder = project
                            break
                    with open("data/assignments.json" , mode='r') as task_file:
                        try:
                            counter =0
                            tasks = json.load (task_file)
                            for task in tasks:
                                if task['name_of_project'] == project_holder['name']:
                                    counter+=1
                                    rprint(str(counter) + '. ' + task['topic'] + ' ID : ' + task['id'])
                            if counter == 0:
                                os.system('cls')
                                print("this project has no task to do")
                                time.sleep(3)
                                uh.Program.menu_after_logging_user(username)
                            choice = input('Enter your choice for assignments (num) : ')
                            if (choice.isdigit()) and int(choice) in range(1, counter + 1):
                                counter =0        
                                for task in tasks:
                                    if task['name_of_project'] == project_holder['name']:
                                        counter+=1
                                        if str(counter) == choice:
                                            os.system('cls')
                                            view.print_task_table(task)
                            while True:
                                choice = input('Enter \'r\' to return : ')
                                if choice == 'r':
                                    uh.Program.menu_after_logging_user(username)
                                else:
                                    print("Enter a valid input")
                        except json.JSONDecodeError:
                            os.system('cls')
                            print("The file is empty")
                            time.sleep(3)
                            uh.Program.menu_after_logging_user(username)
                            
                except json.JSONDecodeError:
                    os.system('cls')
                    print("The file is empty")
                    time.sleep(3)
                    uh.Program.menu_after_logging_user(username)
class PriorityType(Enum):
    CRITICAL = 4
    HIGH = 3
    MEDIUM = 2
    LOW = 1
class StatusType(Enum):
    ARCHIEVED = 5
    DONE = 4
    DOING = 3
    TODO = 2 
    BACKLOG = 1