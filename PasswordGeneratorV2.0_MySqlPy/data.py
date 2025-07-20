#December 26, 2023

import sqlite3
import time

connection = sqlite3.connect('records.db')
cursor = connection.cursor()

try:
    cmd = """CREATE TABLE IF NOT EXISTS data(update_id TEXT, created_on TEXT, name TEXT, username TEXT,
password TEXT, website_app TEXT, last_modified TEXT, remarks TEXT, past_changes TEXT)"""
    cursor.execute(cmd)
    connection.commit()
    print("New Records - data initialized")
except sqlite3.Error as e:
    print("Error:", e)
else:
    #code enters here when there is no exception and try condition(s) are true
    try:
        cmd = "SELECT NAME FROM sqlite_master WHERE type='table' AND name='data'"
        cursor.execute(cmd)
        output = cursor.fetchall()
        #print(output)
        if output[0][0]=='data':
            print("Connection Established")
    except sqlite3.Error as e:
        print("Error while checking table existence:", e)
    #finally:
     #   connection.close()

def update_id():
    x=time.ctime()
    x1=x.replace(" ","")
    x2=x1.replace(":","")
    return x2

def created_on():
    date = f"{time.localtime().tm_mon}/{time.localtime().tm_mday}/{time.localtime().tm_year}"
    return date

def new_record(name,username,password,web_app,last_modified,remarks,past_changes):

    """update_id= update_id()
    created_on= created_on()
    name = input("Name\t")
    username = input("Username\t")
    password = input("Password\t")
    
    #Check_pass framework redesign required
    
    web_app = input("Website/App\t")
    last_modified = ''
    remarks = input("Remarks\t")
    past_changes = ''
"""
    values = (update_id,created_on,name,username,password,web_app,last_modified,remarks,past_changes)
    sql = "INSERT INTO data VALUES('&s','&s','&s','&s','&s','&s','&s','&s','&s')"%values
    cursor.execute(sql)
    print("Record being inserted...\t|\t")
    connection.commit()
    print("Changes saved")

#def update_record(key,value)
    


