#Secure lock your docs/imgs, etc
from display import hold
import os
directory = os.listdir()

    
def menu():
    uio=input("""
_________________________________________________________________________________________________________________________
                                            SECURE LOCK YOUR FOLDERS
                                           ==========================
                                          Offline Solutions by Utkarsh
                                          -----------------------------
                                                    [Options]

            1. Lock Directory  #Under Dev
            2. Unlock Directory  ''
            3. Lock file 
            4. Unlock file
================================
 0. Exit
================================
__________________________________________________________________________________________________________________________
\n""")
    
    if uio==1:
        pass
    elif uio==0:
        exit()
    hold()

class key:
    extension='.locked'
    extension_size = len(extension)
    unlock_ext = -(extension_size)

    def file(name):
        file = open(name,'a')
        return file
    def folder(location):
        pass

class mechanism:
    def lockdir(directory):
        if directory==list:
            pass
        else:
            print("Selected element is not in list format!")
            return
        count=0
        for data in directory:
            data+=key.extension
            directory[count]=data
            count+=1
        return 0

    def unlockdir(directory):
        if directory==list:
            pass
        else:
            print("Selected element is not in list format!")
            return
        count=0
        for data in directory:
            value=key.unlock_ext
            data = data[:value]
            directory[count]=data
            count+=1
        return 1





