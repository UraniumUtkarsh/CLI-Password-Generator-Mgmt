#February 12, 2021
#Password Generator and saver
#fun(x)(s) only

import random

class file():
    """
Use file.<name of function>

Functions~

    alpha() function for alphabet list in lower case
    Alpha() function for alphabet in upper case
    num() function for number list from 0 to 9
    spec() funtion for special character list
    """

    def alpha():
        a=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
        #ord() 97 -> 122 for alpha
        #chr()
        return(a)

    def Alpha():
        A=('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
        #ord() 65 -> 90 for Alpha
        return(A)
    
    def num(x=None):
        l=[]
        if x!=None:
            for i in range(x):
                l.append(i)
            return(l)
        else:
            n=[0,1,2,3,4,5,6,7,8,9]
            return(n)

    def spec():
        s=('!','@','#','$','%','&','*','-','_','+')
        return(s)

class generate():
    def weakP():
        print("\n\t\tWeak Password Generator\n")
        ch=int(input("""\t\tWhich kind of Password would you like to generate?
    1. lower case only
    2. upper case only
    3. numbers only
_______________________
0. Return back
_______________________

    >>>\t"""))
        if ch==1:
            f=file.alpha()
        
            initial=0
            np=[]
            while initial<1:
                for i in range(8):
                    np.append(random.choice(f))
                initial+=1
            #Converting it into usable single string format
            snp=''
            for j in np:
                snp+=j
            
            print("\n Password Generated\t",snp)
            return(snp)
            
            input("Press Enter")

        elif ch==2:
            f=file.Alpha()

            ini=0
            np=[]
            while ini<1:
                for i in range(8):
                    np.append(random.choice(f))
                ini+=1
            #Converting into readable
            snp=''
            for j in np:
                snp+=j
            print("\n Password Generated\t",snp)
            return(snp)
            input("Press Enter")

        elif ch==3:
            f=file.num()

            ini=0
            random.shuffle(f)
            #Converting into readable
            snp=''
            while ini<1:
                for j in f:
                    snp+=str(j)
                ini+=1
            snp=snp[:-2]
            print("\n Password Generated\t",snp)
            return(snp)
            input("Press Enter")

    def medP():
        l1=file.num()
        l2=file.alpha()
        l3=file.Alpha()

        nnum=[]
        nalpha=[]
        nAlpha=[]

        ini=0
        while ini<1:
            for i in range(8):
                nnum.append(random.choice(l1))
                nalpha.append(random.choice(l2))
                nAlpha.append(random.choice(l3))
            ini+=1
        #print(nnum,nalpha,nAlpha)
        #equation values
        ini=0
        while ini<1:
            s1=random.randint(0,8)
            s2=random.randint(s1,8)
            x=s1+s2
            if x<8:
                ini+=1
                s3=8-(s2+s1)
            elif x==8:
                ini+=1
                s3=0
            else:
                pass
        
        #print(s1,s2,s3)
        #equation
        nnum=nnum[:s1]
        nalpha=nalpha[:s2]
        nAlpha=nAlpha[:s3]
        #print(nnum,nalpha,nAlpha)
        #New list defined
        nl=nnum+nalpha+nAlpha
        random.shuffle(nl)
        #Password Generated in list form
        sp=''
        ini=0
        while ini<1:
            for i in nl:
                sp+=str(i)
            ini+=1
        print("\n Password Generated\t",sp)
        return(sp)
        input("Press Enter")

    def strongP(upto):
        #assigning lists
        l1=file.num()
        l2=file.alpha()
        l3=file.Alpha()
        l4=file.spec()
        #list assgnd

        nl1=nl2=nl3=nl4=[]

        #upto=int(input("\nWhat should be the length of Password (8~64)? \t"))
        
        ini=0
        while ini<1:
            for i in range(upto):
                nl1.append(random.choice(l1))
                nl2.append(random.choice(l2))
                nl3.append(random.choice(l3))
                nl4.append(random.choice(l4))
            ini+=1
        #equation values
        ini=0
        while ini<1:
            s1=random.randint(0,upto)
            s2=random.randint(s1,upto)
            x=s1+s2
            if x<upto:
                s3=random.randint(s2,upto)
                y=x+s3
                if y<upto:
                    s4=upto-y
                    ini+=1 #Just this case will pass the values
                else:
                    pass
            else:
                pass
        #values out
        #equation
        nl1=nl1[:s1]
        nl2=nl2[:s2]
        nl3=nl3[:s3]
        nl4=nl4[:s4]
        #new list OK
        nl=nl1+nl2+nl3+nl4
        #new list defined
        random.shuffle(nl)
    
        #Password Generated in list form
        sp=''
        ini=0
        while ini<1:
            for i in nl:
                sp+=str(i)
            ini+=1
        print("\n Password Generated\t",sp)
        return(sp)
        input("Press Enter")



    
    
          
