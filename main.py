from rich import print as rprint
from libs.user import User
import os

os.system('cls')
rprint("Hello , Welcome to Trellomize")
rprint("")
rprint("1.Sign in")
rprint("2.Sign up")

while True:
    rprint("Your choice: ")
    option = int(input())
    if option not in [1,2]:
        rprint("Invalid input . Please try again .")
    else:
        break

if option == 1:
    User.sign_in()
if option == 2:
    User.sign_up()
