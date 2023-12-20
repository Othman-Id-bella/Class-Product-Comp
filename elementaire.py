from produit import * 

class Elementaire(Produite):
    def __init__(self, nom, code, prixAchat):
        super().__init__(nom, code)
        self.__prixAchat = prixAchat

    @property
    def prixAchat(self):
        return self.__prixAchat
    @prixAchat.setter
    def prixAchat(self,other):
         self.__prixAchat=other.__prixAchat

    
