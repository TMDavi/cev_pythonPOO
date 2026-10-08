
class Termostato:

    def __init__(self, temperatura=24):
        self.__temperatura = temperatura
        self.ftemperatura = ''

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, valor):
        if (16 <= valor <= 30) and (valor % 0.5 == 0):
            self.__temperatura = valor
            self.ftemperatura = f"{self.__temperatura}°C"
        elif valor < 16:
            self.__temperatura = 16
            self.ftemperatura = f"{16}°C"
        elif valor > 30:
            self.__temperatura = 30
            self.ftemperatura = f"{30}°C"
        else:
            raise ValueError(f"Temperatura de {valor}°C inválida!")



    

