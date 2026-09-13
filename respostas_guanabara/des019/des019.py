from time import sleep
from rich import print
from rich.traceback import install
install()

class Livro:
    """
    Cria um livro e simula a passagem de páginas
    """

    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas
        self.pagina_atual = 1
        print(f":book: Você acabou de abrir o livro [red]{self.titulo}[/] que tem {self.paginas} páginas no total. Você esta na página [yellow]{self.pagina_atual}[/]")


    def avancar_paginas(self, quant):
        cont = 0
        for pg in range(0, quant, 1):
            if not self.fim_dom_livro():
                self.pagina_atual += 1
                print(f"Pág{self.pagina_atual} :arrow_forward: ", end='')
                sleep(0.2)
                cont += 1
        print(f"\nVocê avançou [yellow]{cont} páginas [/] e agora está na página {self.pagina_atual}")

        if self.fim_dom_livro():
            print(f":closed_book: Você chegou ao final do livro [red]{self.titulo}[/]")


    def fim_dom_livro(self) -> bool:
        return True if self.pagina_atual == self.paginas else False

l1 = Livro("Curso de Python POO", 30)

l1.avancar_paginas(10)
l1.avancar_paginas(10)
l1.avancar_paginas(12)

