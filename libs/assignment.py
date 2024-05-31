import json
import libs.view as view
import libs.Program as uh
import libs.save_user_action as log
import re
import uuid
import time
import os
from pathlib import Path
from rich import print as rprint
from datetime import datetime , timedelta , date
from enum import Enum
""" Here is to add a task
    Remove a task
    Assign a task
    Unassign a task
    Change task properties
    See a task if user is a member of project
"""
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
        if Path("data/projects.json").exists():
            with open("data/projects.json" , mode='r') as project_json:
                try:
                    projects=json.load(project_json)
                except:
                    os.system('cls')
                    rprint("You don't have any projects")
                    time.sleep(3)
                    uh.Program.menu_after_logging_user(username)
                get_name = False
                while not(get_name) :
                    counter =0
                    os.system('cls')
                    rprint("Choose your project to add assignment")

                    for project in projects:
                        if project['leader'] == username:
                            counter+=1
                            rprint(str(counter) + '.[bright_magenta] Name of the project : ' + "[light_sea_green]" +  project['name'] + "[dark_goldenrod] ID of The project : " +"[light_sea_green]"+ project['ID'])
                    if counter ==0:
                            os.system('cls')
                            print("You don't have any project . First make a project")
                            time.sleep(3)
                            uh.Program.menu_after_logging_user(username)        
                    choice = input('Enter your choice  : ')
                    counter = 0
                    for project in projects:
                        if project['leader'] == username:
                            counter +=1
                            if choice == str(counter):
                                id_of_project = project['ID']
                                get_name = True
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
                        priority =4
                        priority = PriorityType(int(priority)).name
                        break
                    if priority == '2' or priority.lower() == "high":
                        priority =3
                        priority = PriorityType(int(priority)).name
                        break
                    if priority == '3' or priority.lower() == "medium":
                        priority =2
                        priority = PriorityType(int(priority)).name
                        break
                    if priority == '4' or priority.lower() == "low":
                        priority = 1
                        priority = PriorityType(int(priority)).name
                        break
                    else:
                        os.system('cls')
                        rprint("Please enter a valid priority")
                        time.sleep(3)
                starting_point = datetime.now()
                deadline = starting_point + timedelta (hours= 24)
                starting_point_str = starting_point.strftime("%Y-%m-%d")
                deadline_str = deadline.strftime("%Y-%m-%d")
                id = str(uuid.uuid4())
                message = username +" created a task."
                new_assignment = Task(topic ,description ,starting_point_str , deadline_str ,id_of_project ,
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
                    'starting_point' : str(starting_point_str),
                    'deadline' : str(deadline_str),
                    'id_of_project' : id_of_project,
                    'id' : id,
                    'assignees' : [],
                    'priority' : priority,
                    'status' : StatusType.BACKLOG.name,
                    'comments' : {}
                }
                with open("data/assignments.json" , mode='w') as task:
                    datas.append(data)
                    json.dump(datas , task , indent=4)
                log.announcement.info(username + " added a task to "  + " project.")
                uh.Program.menu_after_logging_user(username)
    def remove_assignment(username):
        if Path("data/projects.json").exists() and Path("data/assignments.json").exists():
            with open("data/projects.json", mode='r') as feedsjson:
                try:
                    projects = json.load(feedsjson)
                    get_name_of_project = False
                    while not (get_name_of_project):
                        os.system('cls')
                        counter=0
                        for project in projects:
                            if project['leader'] ==username:
                                counter+=1
                                rprint(str(counter) + '. ' + project['name'])
                        if counter == 0:
                            os.system('cls')
                            rprint("You don't have any projects")
                            time.sleep(2)
                            uh.Program.menu_after_logging_user(username)
                        counter =0
                        choice = input('Enter your choice : ')
                        for project in projects:
                            if project['leader'] ==username:
                                counter+=1
                                if choice == str(counter):
                                    get_name_of_project = True
                                    id_of_project = project['id']
                                    break
                        else:
                            os.system('cls')
                            rprint("Please enter a valid name .")
                            time.sleep(3)
                except json.JSONDecodeError:
                    os.system('cls')
                    print("You don't have any projects!")
                    time.sleep(3)
                    uh.Program.menu_after_logging_user(username)
        else:
            rprint("File not found")
            time.sleep(3)
            uh.Program.menu_after_logging_user(username)
        with open("data/assignments.json" , mode='r') as feeds:
            try:
                tasks = json.load(feeds)
                get_name = False
                while not(get_name):
                    os.system('cls')
                    counter=0
                    for task in tasks:
                        if task['id_of_project'] == id_of_project:
                            counter+=1
                            rprint(str(counter) + '. ' + task['topic'])
                    if counter ==0:
                        os.system('cls')
                        rprint("This project has no task to remove")
                        time.sleep(2)
                        uh.Program.menu_after_logging_user(username)
                    choice = input('Enter your choice to remove the task : ')
                    counter =0
                    for task in tasks:
                        if task['id_of_project'] == id_of_project:
                            counter +=1
                            if choice == str(counter):
                                get_name = True
                                target_task = task
                                break
                    else:
                        rprint("Please enter a valid input")
                        time.sleep(2)
                tasks.remove(target_task)
                log.announcement.info(username + " removed a task from a project with " + target_task['id_of_project'] + " ID.")
                with open("data/assignments.json" , mode='w') as updated_file:
                        json.dump(tasks , updated_file , indent=4)
                os.system('cls')
                rprint("The task successfuly has been removed")
                time.sleep(3)                                
                uh.Program.menu_after_logging_user(username)
            except json.JSONDecodeError:
                os.system('cls')
                print("You don't have any projects")
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
                        if counter ==0:
                            os.system('cls')
                            rprint("You don't have any projects")
                            time.sleep(2)
                        choice = input('Enter your choice : ')
                        counter =0
                        for project in projects:
                            if project['leader'] == username:
                                counter +=1
                                if str(counter) == choice :
                                    id_of_project = project['ID']
                        if any ((id_of_project == project['ID'] and len(project['list_of_members']) != 0 ) for project in projects):
                            while True:
                                for project in projects:
                                    if project['ID'] == id_of_project:
                                        for item in project['list_of_members']:
                                            print(item)
                                member_name = input("Enter the member name to add assignment to him/her : ")
                                if any(member_name in project['list_of_members'] for project in projects):
                                    break
                            break
                        if any ((id_of_project == project['ID'] and len(project['list_of_members']) == 0 ) for project in projects):
                            rprint("This project has no member . please choose another one")
                            time.sleep(3)
                        else:
                            os.system('cls')
                            rprint("Please enter a valid name .")
                            time.sleep(3)
                except json.JSONDecodeError:
                    os.system('cls')
                    print("You don't have any projects")
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
                                if task['id_of_project'] == id_of_project:
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
                                    if task['id_of_project'] == id_of_project:
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
        if Path("data/projects.json").exists() and Path("data/assignments.json").exists():
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
                        if counter ==0:
                            os.system('cls')
                            rprint("You don't have any projects .")
                            time.sleep(2)
                            uh.Program.menu_after_logging_user(username)
                        choice = input('Enter your choice : ')
                        counter = 0
                        for project in projects:
                            if project['leader'] == username:
                                counter+=1
                                if str(counter) == choice:
                                    id_of_project = project['ID']
                        if any (project['ID'] == id_of_project for project in projects):
                                with open("data/assignments.json" , mode='r') as task_file:
                                    try:
                                        tasks = json.load(task_file)
                                        while True:
                                            os.system('cls')
                                            counter = 0
                                            for task in tasks:
                                                if task['id_of_project'] == id_of_project:
                                                    counter+=1
                                                    rprint(str(counter) + '. name : ' + task['topic'] + ' ID :' + task['id'])
                                            choice = input('Enter your choice : ')
                                            if not choice.isdigit() or int(choice) not in range(1, counter + 1):
                                                os.system('cls')
                                                rprint("Enter a valid input")
                                                time.sleep(3)
                                            else:
                                                counter=0
                                                for task in tasks:
                                                    if task['id_of_project'] == id_of_project:
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
                                    except:
                                        os.system('cls')
                                        rprint("There is no task for that project")
                                        time.sleep(3)
                                        uh.Program.menu_after_logging_user('cls')
                                        
                except json.JSONDecodeError:
                    os.system('cls')
                    rprint("You don't have any projects")
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
                            print("You don't have any assignments")
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
                        rprint("5.Change Start Point")
                        rprint("6.Change Deadline")
                        rprint("7.Exit this section")
                        choice = input('Enter your choice : ')
                        if choice == '1':
                            assignment = Task.change_priority(assignment)
                            view.print_task_table(assignment)
                            log.announcement.info(username + " changed the priority of the " + assignment['id_of_project'] + " project.")
                        if choice == '2':
                            assignment = Task.change_status(assignment)
                            view.print_task_table(assignment)
                            log.announcement.info(username + " changed the status of the " + assignment['id_of_project'] + " project.")
                        if choice == '3':
                            assignment = Task.add_comment(username  , assignment)
                            view.print_task_table(assignment)
                            log.announcement.info(username + " added a comment to " + assignment['id_of_project'] + " project.")
                        if choice == '4':
                            assignment = Task.change_description(assignment)
                            view.print_task_table(assignment)
                            log.announcement.info(username + " changed the description of the " + assignment['id_of_project'] + " project.")
                        if choice == '5':
                            assignment = Task.change_starting_point(assignment ,username)
                            view.print_task_table(assignment)
                        if choice == '6':
                            assignment = Task.change_deadline(assignment , username)
                            view.print_task_table(assignment)
                        if choice == '7':
                            break   
                        else:
                            print("Enter a valid input")
                    with open("data/assignments.json" , mode='w') as updated_file:
                        json.dump(tasks,updated_file,indent=4)
                    uh.Program.menu_after_logging_user(username)
                except json.JSONDecodeError:
                    os.system('cls')
                    print("File doesn't not have suitable data")
                    time.sleep(3)
                    uh.Program.menu_after_logging_user(username)
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
                    priority = 4
                    priority = PriorityType(int(priority)).name
                    break
                if priority == '2' or priority.lower() == "high":
                    priority = 3
                    priority = PriorityType(int(priority)).name
                    break
                if priority == '3' or priority.lower() == "medium":
                    priority = 2
                    priority = PriorityType(int(priority)).name
                    break
                if priority == '4' or priority.lower() == "low":
                    priority = 1
                    priority = PriorityType(int(priority)).name
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
                    status = 5
                    status = StatusType(int(status)).name
                    break
                if status == '2' or status.lower() == "done":
                    status  = 4
                    status = StatusType(int(status)).name
                    break
                if  status == '3' or status.lower() == "doing":
                    status = 3
                    status = StatusType(int(status)).name
                    break
                if status == '4' or status.lower() == "todo":
                    status = 2
                    status = StatusType(int(status)).name
                    break
                if status == '5' or status.lower() == "BACKLOG":
                    status = 1
                    status = StatusType(int(status)).name
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
    def change_starting_point(assignment , username):
        os.system('cls')
        while True:
            rprint("Enter a number (0,1,...) to set how many days after[red] now [white]should be starting point : ")
            days_after_now = input()
            if (not days_after_now.isdigit()) or int(days_after_now)<0:
                rprint("Please enter a valid input")
            else:
                break
        today = date.today()
        future_date = today + timedelta(days =int(days_after_now) )
        assignment_deadline = datetime.strptime(assignment['deadline'], "%Y-%m-%d").date()
        time_difference = future_date - assignment_deadline
        if time_difference.days > 0:
            rprint("You have to change the deadline too because deadline should be after start point ")
            time.sleep(3)
            assignment = Task.change_deadline(assignment,username)
        assignment['starting_point'] = str(future_date)
        log.announcement.info(username + " changed the starting point of the " + assignment['id_of_project'] + " project.")
        return assignment
        
        
        
    def change_deadline(assignment , username):
        os.system('cls')
        while True:
            rprint("Enter a number (0,1,...) to set how many days after [red] starting point [white] should be deadline : ")
            days_after_start = input()
            if (not days_after_start.isdigit()) or int(days_after_start)<0:
                rprint("Please enter a valid input")
            else:
                break
        start_point = datetime.strptime(assignment['starting_point'], "%Y-%m-%d").date()
        future_date = start_point + timedelta(days=int(days_after_start))

        assignment['deadline'] = str(future_date)
        log.announcement.info(username + " changed the deadline of the " + assignment['id_of_project'] + " project.")
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
                        choice = input('Enter your choice for project  : ')
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
                                if task['id_of_project'] == project_holder['ID']:
                                    counter+=1
                                    rprint(str(counter) + '. ' + task['topic'] + ' ID : ' + task['id'])
                            if counter == 0:
                                os.system('cls')
                                print("this project has no task to see")
                                time.sleep(3)
                                uh.Program.menu_after_logging_user(username)
                            choice = input('Enter your choice  : ')
                            if (choice.isdigit()) and int(choice) in range(1, counter + 1):
                                counter =0        
                                for task in tasks:
                                    if task['id_of_project'] == project_holder['ID']:
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
                            print("You don't have any assignments")
                            time.sleep(3)
                            uh.Program.menu_after_logging_user(username)
                            
                except json.JSONDecodeError:
                    os.system('cls')
                    print("You don't have any projects")
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