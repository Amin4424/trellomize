import json
import libs.view as view
import libs.userhandling as uh
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
                 specific_id , assignees , priority , status , history , comment
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
        self.history = history
        self.comment = comment
    def add_assignment(username):
        with open("data/projects.json" , mode='r') as project_json:
            projects=json.load(project_json)
            counter =0
            get_name=False
            while not(get_name):
                os.system('cls')
                rprint("Choose your project to add assignment")
                for project in projects:
                    if project['leader'] == username:
                        counter+=1
                        rprint(str(counter) + '. ' +  project['name'])
                        name_of_project = input('Enter your choice : ')
                        if name_of_project == project['name']:
                            get_name == True
                        else :
                            os.system('cls')
                            rprint('Please enter a valid name')
                            time.sleep(3)
            topic = input("Enter a topic for the assignment")
            description = input("Enter a description for the assignment")
            while True:
                os.system('cls')
                priority = input("Choose the priority for the task")
                rprint("1.CRITICAL")
                rprint("2.HIGH")
                rprint("3.MEDIUM")
                rprint("4.LOW")
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
                    starting_point = datetime.now().strftime("%Y:%m:%d:%H:%M:%S")
                    deadline = starting_point + timedelta (hours= 24)
                    id = str(uuid.uuid4())
                    message = username +" created a task."
                    history = []
                    history.append(message) 
                new_assignment = Task(topic ,description ,starting_point , deadline ,name_of_project ,
                                      id , [] ,priority , StatusType.BACKLOG ,history , {} )
class PriorityType(Enum):
    CRITICAL = "CRITICAL"
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"
class StatusType(Enum):
    ARCHIEVED = "ARCHIEVED"
    DONE = "DONE"
    DOING = "DOING"
    TODO = "TODO" 
    BACKLOG = "BACKLOG"