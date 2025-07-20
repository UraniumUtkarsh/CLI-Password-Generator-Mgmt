#May 3, 2021
#word Generator

a=97
z=122
A=65
Z=90

class words:
    
    list1=[]
    def letter_1():
        for letters in range(97,123):
            list1.append(chr(letters))
        else:
            file=open("letter_1.txt","w")
            for i in list1:
                file.write(i)
            else:
                print("\nFile with single letters saved in letter_1.txt\n")
        return "Completed..."

    list2=[]
    def letter_2
            
