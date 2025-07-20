def data_out(data):
    inputF=input("New file name with extension: ")
    if inputF.find(".",0,len(inputF)) == -1:
        inputF+=".txt"
        print("'.txt' extension added, file name looks like ",inputF) 
    else:
        pass
    print("Default location: 'C:\\Users\\UPLC\\Desktop\\'")
    yn=input("Would you like to continue with default location? <y/n>\t")
    if yn=='n':
        location=input("Enter location for new file: ")
        if location == '':
            location="C:\\Users\\UPLC\\Desktop\\"
            print("\tDefault locatio selected!")
        else:
            pass
    else:
        location="C:\\Users\\UPLC\\Desktop\\"

    try:
        bind=location+inputF
        file = open(bind,mode='w')
        ret=True
    except:
        print("New Location not accepted, try using double slash '\\'")
        file = open(inputF,mode='w')
        ret=False
        pass
    
    for i in data:
        if type(i) != str:
            i=str(i)
        else:
            pass
        file.write(i)
    else:
        print("File written!")

    file.close()
    return ret
