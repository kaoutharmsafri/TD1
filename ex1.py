import re
adn =input("Entre la chaine ADN:")# accccccccctttta
seq =input("Entre la séquence ADN:")# ac

def saisie(x):
    if not((x=="" or x==" ") or (re.search("[^atgc]", x))):
        print ("la chaîne: ",x)
        return "vraie"
    else :
        print("la chaine est impossible")
        return "faux"
    # for i in x:
    #     if i not in ('a','t','g','c'):
    #         return "faux"
    # return "vraie"

def proportion(x,seq):
    c=0
    if(saisie(x)=="vraie"):
        if(seq in x):
            c+=1
        p=(c/len(x))*100
        print("séquence: ",seq)
        print("il y a %.2f de %s dans vote chaîne."%(p,seq))
    else:
       pass

saisie(adn)
proportion(adn,seq)
