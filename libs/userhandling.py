import json
import libs.view as view
import libs.get_input as input
import libs.project as project
import libs.assignment as ag
from loguru import logger
from pathlib import Path
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
                Program.delete_project(username)
                break
            elif choice == '3':
                Program.working_on_project(username)
                break
            else:
                print("Invalid input.")
    def manager_logging_in(username):
        view.logging_in_message(username)
        logger.add('data/logging.log')
        logger.info(username+ ' just logged into his/her account')
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
    def delete_project(username):
        view.get_name_of_project()
        project.Project.delete_project(username)

    def working_on_project(username):
        view.menu_work_on_project()
        choice = input.get_string()
        while True:
            if choice =='1':
                project.Project.add_member_to_project(username)
            if choice =='2':
                project.Project.remove_member_to_project(username)
            if choice =='3':
                ag.Task.add_assignment(username)
            if choice =='4':
                ag.Task.remove_assignment(username)
            if choice =='5':
                ag.Task.assign_to_member(username)
                