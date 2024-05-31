import os
from time import sleep
from rich import print  as rprint
from rich.table import Table
from rich.console import Console
def wrong_input():
    print(" [steel_blue3][Error]: Please enter a valid input!")

def get_name():
    os.system('cls')
    rprint("[cornflower_blue]Enter your fullname:")

def get_username():
    rprint("[aquamarine1]Enter your username:")

def get_password():
    rprint("[dark_violet]Enter your password:")

def get_email():
    rprint("[dark_magenta]Enter your email:")

def alreay_exist():
    print("[orange4]This username has already exist!\nPlesae enter another one:")
def invalid_email():
    print("Your email is not valid. Please try again:")
def invalid_username_password():
    print("Your username or password is not valid.Please try again.")
    sleep(1)
def sign_in_username():
    rprint("[dodger_blue1]Please enter your username:")
def sign_in_password():
    rprint("[spring_green3]Please enter your password:")
def remove_member_message():
    rprint("Please choose a user to remove from application :")
def logging_in_message(username):
    rprint("[dark_cyan]Welcome dear "+username)
def menu_after_log():
    os.system('cls')
    rprint("1.[green]Create a project")
    rprint("2.[red]Delete a project")
    rprint("3.[blue]Work on a project")
    rprint("4.[blue_violet]Logging out")
def menu_for_manager():
    os.system('cls')
    rprint("1.[yellow]Deactive a user")
    rprint("2.[green]Active a user")
    rprint("3.[red]Delete a user")
    rprint("4[blue_violet].Loging out")
    
def rusure():
    print('[medium_purple]Are you sure?(y/n)')

def get_name_of_project():
    rprint('[wheat1]Enter the name of the project that you want to remove')
def menu_work_on_project():
    os.system('cls')
    rprint("[light_green]1.Add a user to project")
    rprint("2.[light_sky_blue3]Remove a user from a project")
    rprint("[dark_sea_green]3.Add an assignment for project")
    rprint("4.[red]Remove an assignment from project")
    rprint("5.[magenta2]Assign an assignment to a user")
    rprint("6.[light_goldenrod3]Remove assignment from user")
    rprint("7.[sky_blue1]Work on assignment")
    rprint("8.[dark_olive_green3]See all assignments")
    rprint("9[khaki3].Return")
def print_task_table(task):
    console = Console()

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Project ID and Task ID", style="blue", width=15)
    table.add_column("Topic", style="green", width=15)
    table.add_column("Description", style="yellow", width=15)
    table.add_column("Starting Point", style="blue", width=25)  
    table.add_column("Deadline", style="blue", width=25)  
    table.add_column("Assignees", style="magenta", width=30)
    table.add_column("Status", style="cyan", width=15)
    table.add_column("Comments", style="yellow", width=40) 
    table.add_column("Priority", style="green", width=15)

    starting_point = task.get('starting_point', 'N/A')
    deadline = task.get('deadline' , 'N/A')
    comments_str = "\n".join([f"{key}: {value}" for key, value in task['comments'].items()])
    table.add_row(
        task['id_of_project'] + " " + str(task['id']),  
        task['topic'],
        task['description'],
        starting_point,  
        deadline,
        ', '.join(task['assignees']),
        task['status'],
        comments_str, 
        task['priority']
    )

    console.print(table)


def duplicated_user():
    rprint("[yellow]This user has already exist!")
    
def success_sign_up():
    os.system('cls')
    rprint("[green]Your account has been created successfully!")
    rprint("[green]You can sign in with your username and password.")
    sleep(2)
    rprint("[medium_turquoise]This user has already exist!")
    
    
def print_project_table(project):
    console = Console()

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Project Name & ID", style="blue", width=15)
    table.add_column("Owner", style="yellow", width=15)
    table.add_column("Members", style="magenta", width=30)
    table.add_column("Title", style="cyan", width=15)
    
    table.add_row(
        project['name'] + " " + str(project['ID']),  
        project['leader'],
        ', '.join(project['list_of_members']),
        project['title'],)
    console.print(table)