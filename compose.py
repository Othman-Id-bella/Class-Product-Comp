from produit import * 

class Compose(Produite):
    tauxTVA = 0.18

    def __init__(self, nom, code, frais, liste):
        super().__init__(nom, code)
        self.__frais = frais
        self.__liste =liste

    @property
    def getfrais(self):
        return self.frais

    @property
    def getliste(self):
        return self.__liste
    
    @property
    def setfrais(self,other):
         self.__frais=other.__frais

    @property
    def setliste(self,other):
        self.__liste=other.__liste

    def getPrixHT(self):
        prix_ht_constituants = sum(composition.quantite * composition.produit.getPrixHT() for composition in self.__liste)
        prix_ht_total = prix_ht_constituants + self.__frais
        return prix_ht_total
