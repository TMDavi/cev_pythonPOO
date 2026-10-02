from abc import ABC, abstractmethod

class Transporte(ABC):

    def __init__(self, distancia):

        self.distancia = distancia
        self.frete = 0

    @abstractmethod
    def calc_frete(self):
        pass

class Moto(Transporte):
    #distancia livre
    fator=0.5

    def __init__(self,  distancia):
        super().__init__(distancia)
        

    def calc_frete(self):
       self.frete = self.distancia * Moto.fator
       return f"R${self.frete:.2f}"

class Caminhao(Transporte):
    dist = 50
    fator=1.2

    def __init__(self, distancia):
        super().__init__(distancia)
        

    def calc_frete(self):
        if self.distancia >= 50:
            self.frete = self.distancia * Caminhao.fator
            return f"R${self.frete:.2f}"
        else:
            return f"Distancia mínima de {Caminhao.dist}km"

class Drone(Transporte):
    dist = 10
    fator=9.5

    def __init__(self, distancia):
        super().__init__(distancia)
        

    def calc_frete(self):
        if self.distancia <= Drone.dist:
            self.frete = self.distancia * Drone.fator
            return f"R${self.frete:.2f}"
        else:
            return f"Raio máximo de {Drone.dist}km"
