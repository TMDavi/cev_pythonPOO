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

    def tampar(self):
        self.destampado = 0
        return self.destampado
    def destampar(self):
        self.destampado = 1
        return self.destampado

    def quebrarlinha(self, numero=1):
        print(numero*"\n")

    def escrever(self, mensagem):
        if self.destampado == 1:
            print(f"[{self.traduzcor()}]{mensagem}[/] ",end='')
        else:
            print("[red]A caneta ainda está tampada![/]")

c1 = Caneta("amarelo")
c2 = Caneta("roxo")
c3 = Caneta("vermelho")


c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever("Olá mundo!")
c2.escrever("Aprendendo POO!")
c2.quebrarlinha(2)

c3.tampar()
c3.escrever("Quebrando linhas!")
