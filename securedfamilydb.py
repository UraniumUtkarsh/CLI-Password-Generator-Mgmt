from getpass import getpass

#Database security
#=================
            
#Feature Add-on date: June 21, 2021
            
fam_db_safe_ = [] 
def fam_db_safe():
    print("You are accessing confidential data, kindly provide correct family password to the system!")
    password = getpass()
    if password=='':
        print("\n\tNo Password Detected!\n")
        return
    elif password=='family':
        fam_db_safe_.append(1)
        return 1
    else:
        return 0

def fam_db_chk():
    fam_db_safe()
    
    if fam_db_safe_ != []:
        pass
    else:
        fam_db_failure()

def fam_db_failure():
    print("You failed to provide security key!")
    hold()
    exit()
#===========================================================================================================    
