from abc import ABC, abstractmethod

class Porta:

    def abrir(self):
        print(f"Girar a maçaneta e empurrar/puxar a porta")

class Empresa:

    def abrir(self):
        print("Vá ao portal do empreendedor e ...")

class Ovo:

    def abrir(self):
        print("Quebre a casca com um garfo e separe as partes")

class Pedra:
    pass


#Metodo pythonico polimorfico duck typing

def tentar_abrir(objeto):
    try:
        objeto.abrir()
    except:
        print(f"Encontrei problemas ao tentar abrir {objeto.__class__.__name__}")