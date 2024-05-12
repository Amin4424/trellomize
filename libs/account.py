class User:
    username=''
    name=''
    id=''
    pss = ''
    projects = ''
    def __init__(self, usr, pss):
        self.username = usr
        self.pss = pss
        users.append(self)
        users_dic.update({self.username : self.pss})

    def show_menu(self):
        print("hello "+self.username)
        input()
    
    #TODO add user attributes and methods
    
users = []
users_dic = {}
slt = "password_salt"

def exist(usr):
    for item in users:
        if (item.username == usr):
            return True
    return False

def validate(usr, pss):
    if(users_dic[usr] == pss):
        return True
    else:
        return False

def login(usr, pss):
    for item in users:
        if((item.username == usr) and (item.pss == pss)):
            return item
    return ''