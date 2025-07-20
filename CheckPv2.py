#import sqlite3
import time

timestamp = time.ctime()

def create_applog_table():
    connection = sqlite3.connect("logs.db")
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS applog (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            logs TEXT NOT NULL
        )
    ''')

    connection.commit()
    connection.close()

def logger():
    connection = sqlite3.connect("logs.db")
    cursor = connection.cursor()

    cursor.execute('''
        INSERT INTO applog (timestamp,logs)
        VALUES (?, ?)
    ''', (timestamp, logs))

    connection.commit()
    connection.close()


class Check():
    pas = input("Password: ")
    detail = {'haveUp':False, 'haveLow':False,'haveNum':False,'haveSpecial':False,'haveLength':False}
    def chkLen(pas):
        if len(Check.pas)>=8:
            Check.detail['haveLength']=True
            log = f"Check.detail['haveLength'] toggled to {Check.detail['haveLength']}"
            pass
        else:
            log = f"Check.detail['haveLength'] toggled to  {Check.detail['haveLength']}"
            pass
        return log
    
