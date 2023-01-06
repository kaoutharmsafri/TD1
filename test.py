# easy solution without proportion:
def valide(str):
    for c in str:  # On parcourt les caractères de la chaînes.
        if c not in ('a', 't', 'g' ,'c'):  # On teste si 'a', 't', 'g' ou 'c'
            return False
    return True
        
print(valide("attgtaatggtggtacatg")) #True
print(valide("attgraatggtggtacatg")) #False



# ********************************************


#the complete solution but returns the nbr of the sequence not the proportion:
def valide(chaine:list)->bool:
    """vérifie si la chaîne est valide c'est à dire qu'elle n'est pas vide et qu'elle ne contient que des caractères a, t, g et c renvoie True ou false"""
    #print("test valide")
    ens_caracteres = ['a', 't', 'g', 'c']
    if chaine=="":
        return False
    else:
        for caractere in chaine:
            if caractere not in ens_caracteres:
                return False
        return True
def saisie()->str:
    """demande à l'utilisateur de saisir une chaine/séquence valide renvoie cette chaine/séquence"""
    chaine = ""
    while valide(chaine)==False:
        chaine = input("Saisir une chaine d'ADN: ")
    #print(chaine)
    return chaine
def nombre(chaine:str, sequence:str)->float:
    """on cherche le nombre d'occurrences 'sequence' dans 'chaine' on renvoie la fréquence en pourcentage Par exemple : chaîne : 'attgcaatggtggtacatg' séquence : 'ca'-> 2 occurences 'ca' dans 'chaîne'"""
    n = len(chaine)
    m = len(sequence)
    if m > n:
        return 0
    else:
        compteur = 0
        for i in range(n-m+1):
            if chaine[i:i+m]==sequence:
                compteur+=1
        return compteur
###### Programme principal
##chaine = "attgcaatggtggtacatg"
##sequence = "ca"
chaine = saisie()
sequence = input("Saisir une sequence d'ADN: ")
print("Il y a ", nombre(chaine, sequence), " séquence(s) '",\
sequence, "' \ndans la chaîne '", chaine, "'", sep="")


# ******************************************************************


class Date:
    mois = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "aout", "septembre", "octobre", "novembre", "décembre"]
    def __init__(self, jour, mois, annee):
        if 1 <= jour <= 31:
            self.jour = jour
        else:
            raise ValueError('Le jour doit être compris entre 1 et 31')
        if 1 <= mois <= 12:
            self.mois = mois
        else:
            raise ValueError('Le mois doit être compris entre 1 et 12')
        if annee > 1980:
            self.annee = annee
        else:
            raise ValueError("L'année doit être supérieure ou égale à 1980")
        
    def __repr__(self):
        return "%s %s %s" %(self.jour, Date.mois[self.mois-1], self.annee)
        
    def __lt__(self, d):
        if self.annee < d.annee:
            return True
        elif self.annee > d.annee:
            return False
        else:
            if self.mois < d.mois:
                return True
            elif self.mois > d.mois:
                return False
            else:
                return self.jour < d.jour
            
d1 = Date(30, 3, 2020)
d2 = Date(11, 3, 2020)
print(d1 < d2)




# ************************************************************




class CompteBancaire:
    def __init__(self, idNumber, nomPrenom, solde):
        self.idNumber = idNumber
        self.nomPrenom = nomPrenom
        self.solde = solde
        
    def versement(self, argent):
        self.solde = self.solde + argent
        
    def retrait(self, argent):
        if(self.solde < argent):
            print(" Impossiblea d'effectuer l'opération. Solde insuffisant !")
        else:
            self.solde = self.solde - argent

    def agios(self):
        self.solde =self.solde*95/100

    def afficher(self):
        print("Compte numéro : " , self.idNumber)
        print("Nom & Prénom : ", self.nomPrenom)
        print(" Solde  : ", self.solde , " DH ")
        
monCompte = CompteBancaire(16168891, " Bouvier David", 22300)
monCompte.versement(1500)
monCompte.retrait(24000)
#monCompte.agios()
monCompte.afficher()