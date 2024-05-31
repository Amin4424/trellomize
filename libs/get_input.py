from libs.view import rusure as vrusure
from libs.view import wrong_input

def get_username():
    inpt = input()
    
    return inpt

def get_string():
    inpt = input()
    return inpt

def get_integer():
    inpt = input()
    while(input):
        input = get_username()
    return inpt

def rusure():
            while True:
                vrusure()
                inpt = get_string()
                if inpt == 'y' or inpt == 'Y':
                    return True
                if inpt == 'n' or inpt == 'N':
                    return False
                wrong_input()