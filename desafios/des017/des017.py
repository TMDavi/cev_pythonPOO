from rich import print
from rich.panel import Panel

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        box_size = (len(self.nome)+10)
        price_text = f"R${self.preco:,.2f}"
        painel = Panel.fit(f"{self.nome:^{box_size}}\n{box_size*"-":^{box_size}}\n{price_text:.^{box_size}}", 
                       title="Produto")

        print(painel)

p1 = Produto("Iphone 17 Pro Max", 30_000)
p1.etiqueta()

p2 = Produto("Mouse", 100)
p2.etiqueta()