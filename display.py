import time
import random
from printfile import data_out

def hold():
    input()
    return

def uid():
    tim=time.ctime()
    rando=random.randint(100000,999999)
    combo=tim[4:7]
    combo+=tim[8:10]
    #combo shows date now
    combo+=str(rando)
    return combo

def display_line_by_line(data,count=False):
    if count == False:
        for line in data:
            print(line)
    else:
        count=1
        for line in data:
            print(str(count),line)

def print_password_html(password):

    html=f"""
<html>
<head><title>
Python Password Page
<//title>
<//head>
<body bgcolor="black" text="peach">
<marquee bgcolor="red">Welcome to Python generated Password Display page! <//marquee>
<h1><b><center>Your Password is~<BR>
{password}
<//center><//b><//h1>
<//body><//html>"""
    data_out(html)
