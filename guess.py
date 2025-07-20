from passgenfun import file
from display import hold
from printfile import data_out
def menu():
    print()
    pass
O=file.alpha()
sep="\n"

class guess:
    data=[]
    def word2():
        for l1 in O:
            for l2 in O:
                word=l1+l2
                word+=sep
                guess.data.append(word)
            
        data=guess.data      
        return data
    
    def word3():
        for l1 in O:
            for l2 in O:
                for l3 in O:
                    word=l1+l2+l3
                    word+=sep
                    guess.data.append(word)
        data=guess.data
        return data

    def word4():
        for l1 in O:
            for l2 in O:
                for l3 in O:
                    for l4 in O:
                        word=l1+l2+l3+l4
                        word+=sep
                        guess.data.append(word)
        data=guess.data
        return data
                

def make_wordlist():
    data=guess.data
    guess.word2()
    guess.word3()
    guess.word4()
    data_out(data)
    
#out    
#data=guess.word2()
#data_out(data)
