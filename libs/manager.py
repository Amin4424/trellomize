from time import sleep
import viewer
import account

current_user=''

def start():
    if viewer.already_have_account():
        usr=viewer.get_usr()
        pss=hash(viewer.get_pss()+account.slt)
        if account.validate(usr, pss):
            current_user=account.login(usr, pss)
            viewer.succes_login()
            go_to_acc(current_user)
        else:
            viewer.failed_login()
            sleep(2)
            start()
            
def go_to_acc(usr:account.user):
    pass