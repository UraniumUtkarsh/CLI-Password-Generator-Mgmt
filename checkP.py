import string
from passgenfun import file

number=[]
upper=[]
lower=[]
special=[]
repeat=[]
    
class check:

    def numbers():
        return number
    def uppers():
        return upper
    def lowers():
        return lower
    def specials():
        return special
    def repeats():
        return repeat

    #definitions
    #Processing Area
    def findpun(password):
        for i in password:
            for sym in string.punctuation:
                if i == sym:
                    special.append(i)
                    
    def findnum(password):
        nums=[0,1,2,3,4,5,6,7,8,9]
        for i in password:
            for n in nums:
                if i == str(n):
                    number.append(i)
                    
    def findup(password):
        for i in password:
            for u in file.Alpha():
                if i == u:
                    upper.append(i)
                    
    def findlo(password):
        for i in password:
            for l in file.alpha():
                if i == l:
                    lower.append(i)

    
    def findrepeat(password):
        z=0
        i=len(password)
        try:
            while z < i:
                if password[z] == password[z+1]:
                    repeat.append(password[z])
                else:
                    pass
                z+=1
        except:
            pass
        
    #rules
    #Output Area
    def repeatcheck(Password):
        
        if repeat == []:
            return False
        else:
            return repeat,True

    def numcheck(Password):
        
        if number != []:
            return True
        else:
            return False

    def upcheck(Password):
        
        if upper != []:
            return True
        else:
            return False

    def locheck(Password):
        
        if lower != []:
            return True
        else:
            return False

    def specialcheck(Password):
        
        if special == []:
            return False
        else:
            return True

    #Output Area
    def PasswordCheck(Password):
        check.findnum(Password)
        check.findpun(Password)
        check.findlo(Password)
        check.findup(Password)
        check.findrepeat(Password)
        
        #presence check
        p=Password
        rule1=check.numcheck(p)
        rule2=check.upcheck(p)
        rule3=check.locheck(p)
        rule4=check.specialcheck(p)
        rule5=check.repeatcheck(p)
        #rule0 must be 8
        if len(Password)>=8:
            pass
        else:
            print("Password size less than 8 characters!")
            print("Password size must be 8 characters long!")
            return

        #print(rule1,rule2,rule3,rule4,rule5)
        print()

        if rule1 == True and rule2 == True and rule3 == True and rule4 == True and repeat == []:
            print("Valid Password")
            return
        elif rule1==False:
            print("No numbers Used")
        elif rule2==False:
            print("Upper case missing")
        elif rule3==False:
            print("Lower case missing")
        elif rule4==False:
            print("Special character missing")
        elif repeat != []:
            print("Contains repeated elements")
            print(repeat)
        else:
            pass
        
        print("Recreate Password!")
        number.clear()
        lower.clear()
        upper.clear()
        special.clear()
        repeat.clear()

       
