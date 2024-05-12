import libs.account as account

def main_menu():
    print("1 for sign up", "2 for sign in", "3 for exit!", sep="\n")
    return int(input())

def sign_up():
    usr=get_usr()
    while (account.exist(usr)):
        print("This username already exist!")
        usr=get_usr()
    pss=hash(get_pss()+account.slt)
    account.User(usr, pss)
    succes_signup()

def succes_signup():
    pass

def sign_in():
    usr=get_usr()
    pss=hash(get_pss()+account.slt)
    if account.validate(usr, pss):
        succes_login()
        return account.login(usr, pss)
    else:
        failed_login()
        if (whould_try_again()):
            return sign_in()
        else:
            return ''
        
def whould_try_again():
    input = input("Entered username or password was incorrect!", "Would you like to try again?(y/n)", sep="\n").lower()
    if(input=="y"):
        return True
    else:
        return False

def get_usr():
    return input("Enter your username:")

def get_pss():
    return input("Enter your password:")

def succes_login():
    pass

def failed_login():
    pass
