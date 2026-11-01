from abc import ABC, abstractmethod

#Polimorfismo de inclusão 
#Quando um metodo sobrescreve o método da mãe

class Animal(ABC):
    def __init__(self, nome:str=""):
        self.nome = nome

    @abstractmethod
    def emitir_som(self):
        print(f"{self.nome} é {self.__class__.__name__} e está emitindo um som")


class Cachorro(Animal):
    def emitir_som(self):
        print(f"{self.nome} esta fazendo AU AU AU!")

class Spitz(Cachorro):
    pass

class Pitbull(Cachorro):
    pass

class Pato(Animal):
   def emitir_som(self):
        print(f"{self.nome} esta fazendo QUACK QUACK!")

class Gato(Animal):
    def emitir_som(self):
        print(f"{self.nome} esta fazendo MIAU MIAU!")

class Galinha(Animal):
    def emitir_som(self):
        print(f"{self.nome} esta fazendo PO PO PO!")