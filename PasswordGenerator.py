#February 12, 2021
#Password Generator

import passgenfun as fun
import data
from display import hold
from checkP import check
from printfile import data_out
from securedfamilydb import fam_db_chk

while True:
    print("""
                                    Warm Greeting by Password Generator :P
                                    ======================================

            1. Generate only a random Password
            2. Generate - Manage and save a Password
            3. Show Saved Accounts and Passwords
            4. Check how strong your Password is!
-------------------------------------------------------------------------------------------------------------------------
    0. STOP
_________________________________________________________________________________________________________________________
""")
    cin=int(input("Command@ "))
    if cin==0:
        break
    elif cin==1:
        while True:
            ptype=input("""
    Que. Which Type of Password would you like to generate?
         Weak
         Medium
         Strong
         
         ========
          return
         ========
                                                                                                
    Ans. """)
            if ptype=='Weak' or ptype=='weak':
                password=fun.generate.weakP()
                hold()
                break
            elif ptype=='Medium' or ptype=='medium':
                password=fun.generate.medP()
                hold()
                break
            elif ptype=='strong' or ptype=="Strong":
                upto=int(input("\nWhat should be the length of Password (8~64)?"))
                password=fun.generate.strongP(upto)
                hold()
                break
            elif ptype=='return' or ptype=='Return':
                break
            else:
                print("Nothing Selected!")
                hold()
                break
        out=input("Would you like to save this password? <y/n>\t") #Feature tested
        if out == 'y':
            data_out(password)
        else:
            pass
              

    elif cin==2:
        data.menu()
        hold()
    elif cin==3: #Secured
        fam_db_chk()
        data.show_saved()
        hold()
    elif cin==4:
        Password=input("\nEnter your Password to be checked: ")
        print("\nResults~\n")
        run=check.PasswordCheck(Password)
        hold()
        
    else:
        print("No choice selected\n")
        pass
