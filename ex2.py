class Date:
    def __init__(self,jour,m,annee):
        self.jour=jour
        self.mois=["janvier","fevrier","mars","avril","mai","juin","juillet","aout","septembre","octobre","novembre","decembre"]
        self.annee=annee
        for i in range (1,len(self.mois)+1):
            if(m==i):
                self.mois=self.mois[i-1]
            if (m>12 or m<1):
                raise Exception("Sorry, this month is impossible for")
        if(int(jour)>31 or int(jour)<1):
            raise Exception("Sorry, this day is impossible") 

    
    def __repr__(self):
        return str (self.jour)+" "+str (self.mois)+" "+str (self.annee)

    def __lt__(self,d):
        if(self.annee<d.annee):
            return True
        elif(self.annee==d.annee):
            if(self.mois<d.mois):
                return True
            elif(self.mois==d.mois):
                if(self.jour<d.jour):
                    return True
        return False

d1=Date(25,1,2002)
d2=Date(10,1,2002)
print(d1)
print(d1<d2)
