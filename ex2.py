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

    def __it__(self,date):
        if(self.annee==date.annee):
            if(self.mois==date.mois):
                if(self.jour<date.jour):
                    print(self.__repr__()," < ",date.__repr__())
                elif(self.jour>date.jour):
                    print(self.__repr__()," > ",date.__repr__())
                else:
                    print("les deux dates sont identiques")
            elif(self.mois<date.mois):
                    print(self.__repr__()," < ",date.__repr__())
            else:
                    print(self.__repr__()," > ",date.__repr__())
        elif(self.annee<date.annee):
                    print(self.__repr__()," < ",date.__repr__())
        else:
                    print(self.__repr__()," > ",date.__repr__())

    def __expression__(self,date):
        if(self.annee==date.annee):
            if(self.mois==date.mois):
                if(self.jour<date.jour):
                    print(self.__repr__()," < ",date.__repr__()," True")
                elif(self.jour>date.jour):
                    print(self.__repr__()," < ",date.__repr__()," False")
                else:
                    print(self.__repr__()," < ",date.__repr__()," False")
            elif(self.mois<date.mois):
                    print(self.__repr__()," < ",date.__repr__()," True")
            else:
                    print(self.__repr__()," < ",date.__repr__()," False")
        elif(self.annee<date.annee):
                    print(self.__repr__()," < ",date.__repr__()," True")
        else:
                    print(self.__repr__()," < ",date.__repr__()," False")

     


date1=Date(31,7,2001)
date2=Date(1,1,2023)

print("date 1 = ",date1.__repr__())
date1.__it__(date2)
date1.__expression__(date2)
