from rich import print as rprint
from libs.user import User
import os

os.system('cls')
rprint("Hello , Welcome to Trellomize")
rprint("")

while True:
    rprint("1.Sign in")
    rprint("2.Sign up")
    rprint("3.Exit")
    rprint("Your choice: ")
    option = input()
    if option == '1':
        User.sign_in()
        os.system("cls")
    if option == '2':
        User.sign_up()
        os.system("cls")
    if option == '3':
        break
    if option not in ['1','2','3']:
        os.system("cls")
        rprint("Invalid input! Please try again.")