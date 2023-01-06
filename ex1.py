import re
adn=input("Entrer la chaine ADN: ")
search=input("Entrer la séquence ADN que vous cherchez: ")

def saisie(x):
    if not((x=="" or x==" ") or (re.search("[bdefhjklmnopqrsuvwxz]", x))):
        print("vraie")
        return "vraie"
    else:
        print("faux")
        return "faux"

def proportion(x,seq):
    a=0
    if (saisie(x)=="vraie"):
        if(seq in x):
            a+=1
        p=a/len(x) *100
        print("chaîne: ",x)
        print("séquence: ",seq)
        print("il y a %.2f"%p,"% ","de '",seq,"' dans votre chaîne.")
    else:
        print("la saisie est invalide by")
        pass

proportion(adn,search)