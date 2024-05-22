import json
import libs.view as view
import libs.get_input as input
import libs.userhandling as uh
from pathlib import Path
import re
import uuid
from datetime import datetime
#datetime.now().strftime("%Y:%m:%d:%H:%M:%S")
class Project:
    def __init__(self,name,title,leadername,ID):
        self.leadername=leadername
        self.name = name
        self.title = title
        self.ID=ID
        # self.assignment_id = assignment_id
        # self.description = description
        # self.start_point = start_point
        # self.deadline = deadline
    def create_project(leadername,name,title,ID):
        project = Project(leadername,name,title,ID)
        if Path("data/project.json").exists():
            with open("data/project.json", mode='r') as projects:
                try:
                    datas = json.load(projects)
                except json.JSONDecodeError:
                    datas = []
        with open("data/project.json",mode='w') as projects:
            data = {
            'leader': leadername,
            'name': name,
            'title': title,
            'ID': ID
        }
            datas.append(data)
            json.dump(datas, projects, indent=4)            
            
              
                    
            
            