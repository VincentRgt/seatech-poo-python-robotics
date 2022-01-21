import time
from webbrowser import get

class Human():
    __sexe="pas de sexe"
    __estomac=[]

# Constructor
    def __init__(self, sexe):
        if sexe:
            self.__sexe = sexe
        
# Destructor
    def __del__(self):
        print("humain destructor")
# Manger
    def manger(self,aliments):
        if type(aliments)==str:
            print(aliments, ":mangé")
            time.sleep(1)
            self.__estomac.append(aliments)
        else:
            for i in aliments:
                print("%s : mangé"%i)
                time.sleep(1)
                self.__estomac.append(i)

    @property
    def sexe(self):
        return self.__sexe

    @property
    def estomac(self):
        return self.__estomac