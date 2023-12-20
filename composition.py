class Composition:
    def __init__(self,produit,quantite) :
        self.__produit=produit
        self.__quantite=quantite
        
    @property
    def getProduit(self):
        return self.__produit
    @property
    def setPoduit(self,other):
        self.__produit=other.__produit

    @property
    def getQuantite(self):
        return self.__quantite
    @property
    def setQuantite(self,other):
        self.__quantite=other.__quantite

    def __str__(self):
        return f" Composition :Produit, {self.__produit} Quantite,{self.__quantite}"    
    
    def __eq__(self,other):
        return (self.__produit==other.__produit) and (self.__quantite==other.__quantite)
        