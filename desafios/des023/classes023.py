from abc import ABC, abstractmethod
from math import pi

class Poligono(ABC):

    def __init__(self, qtd_lados):
        self.qtd_lados = qtd_lados

    @abstractmethod
    def perimetro(self) -> float:
        pass

    @abstractmethod
    def area(self) -> float:
        pass

class Quadrado(Poligono):

    def __init__(self, lados, qtd_lados=4):
        super().__init__(qtd_lados=4)
        self.lados = lados

    def perimetro(self):
        return self.lados * 4
    
    def area(self):
        return self.lados * self.lados

class Circulo(Poligono):

    def __init__(self, raio):
        super().__init__(qtd_lados=0)
        self.raio = raio

    def perimetro(self):
        return 2 * pi * self.raio 
    
    def area(self):
         return pi * self.raio * self.raio