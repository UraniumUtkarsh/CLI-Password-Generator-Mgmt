#May 7, 2021

import passgenfun as fun
import mysql.connector as co
import time as t
from display import hold,uid,display_line_by_line
from printfile import data_out #not used
from checkP import check
from securedfamilydb import fam_db_chk

#December 4, 2023 - tabulate add on
from tabulate import tabulate

PasswordCheck=check.PasswordCheck
lbl=display_line_by_line

def menu():
    while True:
        print("\n"*10)
        print(""""
__________________________________________________________________________________________________________________________
                                    ************************************************************
                                    ============================================================
                                    Customize - Generate - Save and Manage your Family Passwords
                                                (Offline IT Solutions by Utkarsh)
                                    ------------------------------------------------------------
                                                            [OPTIONS]

     New? - 1         Update? - 2        Generate but don't save? - 3       Show Saved? - 4         DELETE? - 5

     Search By Name     - 6
     Search By Username - 7
     Search By Website  - 8
     
--------------------------------------------------------------------------------------------------------------------------
                                                        Exit? - 0
__________________________________________________________________________________________________________________________
    \n""")
    
        sel=int(input("Command Number?\t"))
        if sel==0:
            break
        elif sel==1:
            new_save()
            hold()
        elif sel==2:
            update()
            hold()
        elif sel==3:
            
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
                    fun.generate.weakP()
                    hold()
                    break
                elif ptype=='Medium' or ptype=='medium':
                    fun.generate.medP()
                    hold()
                    break
                elif ptype=='strong' or ptype=="Strong":
                    upto=int(input("\nWhat should be the length of Password (8~64)?"))
                    fun.generate.strongP(upto)
                    hold()
                    break
                elif ptype=='return' or ptype=='Return':
                    break
                else:
                    print("Nothing Selected!")
                    break
                  

        elif sel==4:
            fam_db_chk()
            show_saved()
            hold()
        elif sel==5:
            delete_saved()
            hold()
        elif sel==6:
            name=input("Name of the Person to search for: ")
            srch=search('name',name)
            lbl(srch)
            hold()
        elif sel==7:
            Username=input("Search by Username: ")
            srch=search('username',Username)
            lbl(srch)
            hold()
        elif sel==8:
            website=input("Search by website: ")
            srch=search('website',website)
            lbl(srch)
            hold()
       
        else:
            print("Invalid Selection!\n\n")
            menu()
            

def search(element,value):
    try:
        connection=co.connect(host="localhost",user="root",passwd="root",database="savedpasswords")
        cursor=connection.cursor()
        valid=['name','website','username','date']
        if element in valid:
            pass
        else:
            #print("No such elements found!")
            return "Invalid"
        vals=(element,value)
        sql="SELECT * FROM data WHERE %s = '%s'"%vals
        cursor.execute(sql)
        data=cursor.fetchall()
        connection.close()
        return data
    except:
        return False


                
            
def show_saved(): #Secured
    try:
        connection=co.connect(host="localhost",user="root",passwd="root",database="savedpasswords")
        cursor=connection.cursor()
            
        sql="SELECT * FROM data"
        cursor.execute(sql)
        _data=cursor.fetchall()
        #print(_data)#debug1
        #_____________________________________________________________________________________________-
        headers=list(_data[0])
        _table = _data[1:]

       #Version1.1

        #count=0
        #print("""
 #Count  Name  Username  Password  Website/App    Last Modified      Update_id          Remarks
 #""")
  #      for rows in _data:
   #         count+=1
            #print(rows)
    #        row=[f'{count}',rows[0],rows[1],rows[2],rows[3],rows[4]]
     #       print("""
#| {} | {} |{} | {} | {} | {} | {} | {} |""".format(f'{count}',rows[0],rows[1],rows[2],rows[3],rows[4],rows[5],row[6]))
        #version1.1 //

        #V2.1
        print(tabulate(_table, headers))
        #V2.1 //

        connection.close()
        return True
    except Exception as e:
        #print("Some error occured!")
        print(e)
        return False

def new_save():
    name=input("Name of the person?\t")
    username=input("Username used <if any> ?\t")
    if username=="" or username==" ":
        username="N/A"
    website=input("Website name: ")
    #Remarks feature add on 6-9-21
    remarks=input("Remarks: ")
    if remarks == '':
        remarks="N/A"
        
    pswd_type=int(input("""
Password Type?
    1. Customized? <Of your choice>
    2. Auto-Generate? <System Generated!>

Choose one of them~ """))
    unid=uid()
    if pswd_type==" " or pswd_type=="":
        #exitf()
        pass
        
    elif pswd_type==1:
        cstz_pswd=input("Your Password here: ")
        PasswordCheck(cstz_pswd)
        action=input("\nWould you like to continue? <y/n>\t")
        action.lower()
        if action=="" or action=="y" or action=="yes":
            pass
        else:
            return
        confirm=input("Confirm Password: ")
        if cstz_pswd == confirm:
            password = confirm
            pass
        else:
            print("\nConfirm Password does not match!\n")
            return
    elif pswd_type==2:
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
                break
                
            elif ptype=='Medium' or ptype=='medium':
                password=fun.generate.medP()
                break

            elif ptype=='strong' or ptype=="Strong":
                password=fun.generate.strongP(10)#why fixed
                break

            elif ptype.lower()=='return':
                return

            else:
                print("Nothing Selected!")
                break
                

        print(f"Your auto-generated password is {password}")
    time=t.ctime()
    print(unid,type(unid),len(unid))
    try:
        connection=co.connect(host="localhost",user="root",passwd="root",database="savedpasswords")
        cursor=connection.cursor()
        count=0
        vals=(count,name,username,password,website,time,unid,remarks)
        sql="INSERT INTO data VALUES('%s','%s','%s','%s','%s','%s','%s','%s')"%vals
        cursor.execute(sql)
        connection.commit()
        connection.close()
        print("Data Saved Successfully!")
        return True
    except Exception as e:
        #print("Some error occured while saving new changes to database!") 
        print(e)#added on Aug 20
        return False


            
def update():
    fam_db_chk()#Secured
    show_saved()
    print("""
 What categories you can change~

         name
         username
         password
         website
         remarks
\n""")
    try:
        connection=co.connect(host="localhost",user="root",passwd="root",database="savedpasswords")
        cursor=connection.cursor()
        update_category=input("What would you like to update?\t")
        update_category.lower()

        uid=input("Confirm update_id: ")
        sql="SELECT * FROM data where update_id='%s'"%(uid)
        cursor.execute(sql)
        data=cursor.fetchone()
        print(data,end="\n")
        
        update_val=input("What is the updated value: ")
        time=t.ctime()

        def updt(tim,uid): #Updates Last Modified! | OK Tested
            val=(tim,uid)
            sql="UPDATE data SET time='%s' WHERE update_id='%s'"%(val)
            cursor.execute(sql)
            connection.commit()
            print(f"Last modified at {tim}")
            connection.close()

        
        sql="UPDATE data SET %s='%s' WHERE update_id='%s'"%(update_category,update_val,uid)
        cursor.execute(sql)
        connection.commit()
        print(f"{update_category} changed to {update_val} at update_id = {uid}")
        updt(time,uid)
        return True
    except Exception as e:
        print("E[Update]'Fail'")
        print("Error code: ",e)
        return False
        

def delete_saved():
    print()
    fam_db_chk()#Secured
    show_saved()
    print()
    try:
        connection=co.connect(host="localhost",user="root",passwd="root",database="savedpasswords")
        cursor=connection.cursor()
        uid=input("update_id of account you wish to delete: ")

        sql="DELETE FROM data WHERE update_id='%s'"%uid
        cursor.execute(sql)
        connection.commit()
        connection.close()
        print(f"Account at update_id {uid} deleted successfully")
        return True
    except:
        print("EDel[savd]01")
        return False
    
