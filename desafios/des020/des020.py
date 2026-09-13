from rich import print
from rich.panel import Panel
from rich.traceback import install

class Gamer:

    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.jogos_favoritos = list()

    def add_jogos(self, jogo):
        return self.jogos_favoritos.append(str(jogo))

    def organiza(self):
        return sorted(self.jogos_favoritos)

    def extrai_jogos(self):
        string = ""
        for j in self.organiza():
            string += f":video_game: {j}\n"

        return string
    
    def ficha(self):

        painel = Panel.fit(f"Nome real: [white on blue] {self.nome} [/]\nJogos favoritos:\n{self.extrai_jogos()}",title=f"Jogador <{self.nick}>") 
        print(painel)


j1= Gamer("Jeremias Neto", "Flavinho do Pneu")
j1.add_jogos("Disc Elysium")
j1.add_jogos("Hades")
j1.add_jogos("Hollow Knight")
j1.add_jogos("Bloodborne")
j1.ficha()

j2= Gamer("Alyssa Liu", "Bode motorizado")
j2.add_jogos("Metro Exodus")
j2.add_jogos("Monster Hunter Wilds")
j2.add_jogos("The return of Obra Dinn")
j2.add_jogos("Peak")
j2.ficha()

