from abc import ABC, abstractmethod

class Numero:

    def __init__(self, valor:int|float = 0):
        self.valor = valor

    def dobrar(self):
        self.valor = self.valor + self.valor
    def __str__(self):
        return f"Tenho o número {self.valor} dentro do numero"

class Lista:

    def __init__(self, lst:list=[]):
        self.valores = lst

    def dobrar(self):
        self.valores = self.valores + self.valores

    def __str__(self):
        return f"Tenho os valores {self.valores} dentro da lista"

class Texto:

    def __init__(self, txt:str = ""):
        self.txt = txt

    def dobrar(self):
        self.txt = self.txt + " " + self.txt

    def __str__(self):
        return f"Tenho o texto {self.txt} dentro do texto"

class Papel:

    def __init__(self):
        self.dobrado = False

    def dobrar(self):
        self.dobrado = True

    def __str__(self):
        return f"O papel esta dobrado? {self.dobrado}"

class Casa:

    def __init__(self):
        pass

    def __str__(self):
        return f"Era uma casa muito engraçada"

#DUCK TYPING

def tente_dobrar(objeto):
    try:
        objeto.dobrar()

    except:
        print(f"Não consegui dobrar {objeto.__class__.__name__}")