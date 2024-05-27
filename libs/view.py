import os
from time import sleep
from rich import print  as rprint
from rich.table import Table
from rich.console import Console
def wrong_input():
    print("Please enter a valid input!")

def get_name():
    os.system('cls')
    print("Enter your fullname:")

def get_username():
    print("Enter your username:")

def get_password():
    print("Enter your password:")

def get_email():
    print("Enter your email:")

def alreay_exist():
    print("This username has already exist!\nPlesae enter another one:")
def invalid_email():
    print("Your email is not valid. Please try again:")
def invalid_username_password():
    print("Your username or password is not valid.Please try again.")
    sleep(1)
def sign_in_username():
    print("Please enter your username:")
def sign_in_password():
    print("Please enter your password:")
def remove_member_message():
    print("Please choose a user to remove from application :")
def logging_in_message(username):
    print("Welcome dear "+username)
def menu_after_log():
    os.system('cls')
    rprint("1.[green]Create a project")
    rprint("2.[red]Delete a project")
    rprint("3.[blue]Work on a project")
    rprint("4.Loging out")
def menu_for_manager():
    os.system('cls')
    rprint("1.[yellow]Deactive a user")
    rprint("2.[green]Active a user")
    rprint("3.[red]Delete a user")
    rprint("4.Loging out")
    
def rusure():
    print('Are you sure?(y/n)')

def get_name_of_project():
    rprint('Enter the name of the project that you want to remove')
def menu_work_on_project():
    os.system('cls')
    rprint("[green]1.Add a user to project")
    rprint("2.[red]Remove a user from a project")
    rprint("[green]3.Add an assignment for project")
    rprint("4.[red]Remove an assignment from project")
    rprint("5.Assign an assignment to a user")
    rprint("6.Remove assignment from user")
    rprint("7.Work on assignment")
    rprint("8.See all projects")
def print_task_table(task):
    console = Console()

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Project Name and Task ID", style="blue", width=15)
    table.add_column("Topic", style="green", width=15)
    table.add_column("Description", style="yellow", width=50)
    # table.add_column("Starting Point", style="blue", width=25)  # Uncomment if needed
    table.add_column("Assignees", style="magenta", width=30)
    table.add_column("Status", style="cyan", width=15)
    table.add_column("Comments", style="yellow", width=50)  # Moved "Comments" before "Priority"
    table.add_column("Priority", style="green", width=15)

    starting_point = task.get('starting_point', 'N/A')
    comments_str = "\n".join([f"{key}: {value}" for key, value in task['comments'].items()])
    table.add_row(
        task['name_of_project'] + " " + str(task['id']),  
        task['topic'],
        task['description'],
        # starting_point,  # Uncomment if needed
        ', '.join(task['assignees']),
        task['status'],
        comments_str,  # Moved comments before priority
        task['priority']
    )

    console.print(table)

    # rprint("6.Work on assignment")

def duplicated_user():
    rprint("[yellow]This user has already exist!")
    
def secces_sign_up():
    rprint("[green]Your account has been created successfully!")
    rprint("[green]You can sign in with your username and password.")
    sleep(2)
    rprint("This user has already exist!")
