from abc import ABC, abstractmethod

class Produite(ABC):
    def __init__(self, nom, code):
        self.__nom = nom
        self.__code = code

    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self,other):
        self.__nom=other

    @property
    def code(self):
        return self.__code
    @code.setter
    def code(self,other):
        self.__code=other.__code

    @abstractmethod
    def getPrixHT(self):
        pass

    def __str__(self):
        return f"Produite: Nom({self.__nom}), Code({self.__code})"

    def __eq__(self,other):
            return self.__nom == other.nom and self.__code == other.code
        