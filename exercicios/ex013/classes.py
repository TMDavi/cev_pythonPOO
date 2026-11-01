from abc import ABC, abstractmethod

class Mae:
    def __init__(self, nome:str=""):
        self.nome = nome

    def fazer_pudim(self):
        print(f"{self.nome} faz pudim com leite condensado")

    def frita_coxinha(self):
        print(f"{self.nome} frita coxinha com oleo de soja")

class Filho(Mae):
    def frita_coxinha(self):
        print(f"{self.nome} frita coxinha cna air fryer")

class Filha(Mae):
    def fazer_pudim(self):
        print(f"{self.nome} faz pudim com leite ninho com nutela")