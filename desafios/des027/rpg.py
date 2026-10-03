from abc import ABC, abstractmethod
import random
from rich import print

class Personagem(ABC):

    morto = 0

    def __init__(self, nome, vida, golpes=[]):
        self.nome = nome
        self.vida = vida
        self.golpes = golpes
        self.vida_max = vida
        self.vida_min = 0

    def acessar_golpe(self):
        return random.choice(self.golpes)

    def morre(self):
        if not Personagem.morto:
            Personagem.morto = 1
        return Personagem.morto 

    def atacar(self, alvo, forca):
        porcent_forca = random.randint(1,101)
        dano = forca*(porcent_forca/100)

        #Imprime mensagem na tela
        print(f"[green]{self.nome}[/][blue]({self.vida})[/] atacou [red]{alvo.nome}[/][blue]({alvo.vida})[/] com um [blue]{self.acessar_golpe()}[/] de força [blue]{forca}[/]")
        print(f"[blue]{alvo.nome}[/] recebeu dano de [red]{dano}[/]!")
        #Alvo recebe o dano
        alvo.receber_dano(dano)

    def receber_dano(self, dano):
        self.vida = self.vida - dano
        if (self.vida - dano) < self.vida_min:
            dano_final = self.vida - self.vida_min
            self.morre()
            self.vida = 0 
            print(f"[red]{self.nome} morreu[/]!")
        else:
            return self.vida 


    @abstractmethod
    def curar(self):
        pass

class Guerreiro(Personagem):
    def __init__(self, nome, vida, golpes=[]):
        super().__init__(nome, vida, golpes=[])
        self.golpes = ["Soco","Chute", "Espadada", "Machadada", "Fúria Espartana"]

    def curar(self):
        cura = random.randint(1,500)
        cura_final = 0

        if (self.vida + cura) > self.vida_max:
            cura_final = self.vida_max - self.vida 
        else:
            cura_final = cura

        self.vida = self.vida + cura_final
        print(f"[blue]{self.nome}[/] tomou uma [yellow]Poção de cura[/] e recuperou {cura_final} pontos de vida")

class Mago(Personagem):
    def __init__(self, nome, vida, golpes=[]):
        super().__init__(nome, vida, golpes=[])
        self.golpes = ["Infinito","Soco", "Raio Azul", "Raio Vermelho", "Vazio roxo"]

    def curar(self):
        cura = random.randint(1,1000)
        cura_final = 0 

        if (self.vida + cura) > self.vida_max:
            cura_final = self.vida_max - self.vida 
        else:
            cura_final = cura

        self.vida = self.vida + cura_final

        print(f"[blue]{self.nome}[/] fez uma [yellow]Magia de cura[/] e recuperou {cura_final} pontos de vida")