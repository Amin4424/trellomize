# import libs.manager as manager
import libs.viewer as viewer
import libs.utils as utils
import libs.account as account
# viewer.welcome()
choose = utils.state(0)
while(choose != utils.state(3)):
    curren_user = ''
    choose=utils.state(viewer.main_menu())
    if(choose == utils.state(1)):
        viewer.sign_up()
    elif(choose == utils.state(2)):
        curren_user = viewer.sign_in()
    if(curren_user != ''):
        curren_user.show_menu()