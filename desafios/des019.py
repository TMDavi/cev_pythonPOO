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

    def __str__(self):
        return f":book: Você acabou de abrir o livro [red]{self.titulo}[/] que tem {self.paginas} páginas no total. Você esta na página [yellow]{self.pagina_atual}[/]"

    def avancar_paginas(self, numero):
        pagina_seguinte = self.pagina_atual + numero

        if self.pagina_atual == 1:
            print(self.__str__())

        if pagina_seguinte <= self.paginas:
            while self.pagina_atual < pagina_seguinte:
                self.pagina_atual += 1
                print(f"Pág{self.pagina_atual} :arrow_forward: ", end="") 
                sleep(0.4)
            print(f"Você avançou [blue]{numero} páginas[/] e agora está na [yellow]página {self.pagina_atual}[/]")

        else:
            restante = self.paginas - self.pagina_atual

            while self.pagina_atual < self.paginas:
                self.pagina_atual += 1
                print(f"Pág{self.pagina_atual} :arrow_forward: ", end="") 
                sleep(0.4)

            print(f"Você avançou [blue]{restante} páginas[/] [red]e chegou no final![/]")
        

l1 = Livro("Curso de Python POO", 30)

l1.avancar_paginas(5)
l1.avancar_paginas(10)
l1.avancar_paginas(10)
l1.avancar_paginas(25)
