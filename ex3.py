class  CompteBancaire:
    def __init__(self,nom,numeroCompte,solde):
        self.nom=nom
        self.numeroCompte=numeroCompte
        self.solde=solde
    
    def versement(self,v):
        self.solde+=v

    def retrait(self,r):
        self.solde-=r

    def agios(self):
        self.solde*=0.95

    def afficher(self):#__repr__
        return "le nom :"+self.nom+" de N° "+str(self.numeroCompte)+" du solde: "+str(self.solde)

c1=CompteBancaire("Sara fzef",101,25000)
print(c1.afficher())
c1.agios()
c1.retrait(5000)
c1.versement(2000)
print(c1.afficher())
