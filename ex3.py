class CompteBancaire:
    numeroCompte=0
    nom=""
    solde=0.0

    def __init__(self,numeroCompte,nom,solde):
        self.numeroCompte=numeroCompte
        self.nom=nom
        self.solde=solde

    def Versement(self,versement):
        self.solde+=versement
        print("le client ",self.nom," de numero de compte %d"%self.numeroCompte," a versé %.2f"%versement)

    def Retrait(self,retrait) :
        self.solde-=retrait
        print("le client ",self.nom," de numero de compte %d"%self.numeroCompte," a retiré %.2f"%retrait)

    def Agios(self):
        # permettant d'appliquer les agios à un pourcentage de 5 % du solde
        agios=self.solde*0.05
        self.solde+=agios
        print("le compte %d"%self.numeroCompte," a des agios du montant %.2f"%agios," donc le solde du compte devient : %.2f"%self.solde)

    def afficher(self):
        # permettant d’afficher les détails sur le compte
        return "le compte N°"+str(self.numeroCompte)+" du client "+self.nom+" a comme solde %.2f"%self.solde

c1=CompteBancaire(102,"Mohamed",5000)
print(c1.afficher()) 
c1.Versement(200.5)
c1.Retrait(50)
print(c1.afficher()) 
c1.Agios()