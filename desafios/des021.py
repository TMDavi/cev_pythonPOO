from rich import print
from translate import Translator
from rich.panel import Panel
from rich.traceback import install

install()

class Caneta:

    destampado = 0

    def __init__(self, cor):
        self.cor = cor

    def traduzcor(self):
        tradutor = Translator(from_lang="pt", to_lang="en")
        resultado = tradutor.translate(self.cor)
        return resultado.lower()

    def destampar(self):
        self.destampado = 1
        return self.destampado

    def quebrarlinha(self, numero=1):
        print(numero*"\n")

    def escrever(self, mensagem):
        if self.destampado == 1:
            print(f"[{self.traduzcor()}]{mensagem}[/]")
        else:
            print("[red]A caneta ainda está tampada![/]")



c1 = Caneta("amarelo")
c1.destampar()
c1.escrever("Olá mundo!")
c1.quebrarlinha()
c1.escrever("Aprendendo a programar em POO")

c2 = Caneta("roxo")
c2.destampar()
c2.escrever("Criando umas bobeiras por aqui")
c2.quebrarlinha(5)
c2.escrever("Escrevendo na cor roxa")


#tradutor = Translator(from_lang="en", to_lang="pt")
#resultado = tradutor.translate(self.cor)
