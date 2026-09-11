from rich import print
from rich.panel import Panel
from rich.traceback import install
install()

#Considere que cada pessoa consome 400 g de carne
#COnsidere que a carne custa R$82,4/kg

class Churrasco:

    quant_carne_por_pessoa = 0.4
    quilo_carne = 82.4

    def __init__(self, titulo, quant):
        self.titulo = titulo
        self.quant = quant

    def carnetotal(self):
        return self.quant * self.quant_carne_por_pessoa

    def precototal(self):
        return self.carnetotal() * self.quilo_carne

    def precopessoa(self):
        return self.precototal() / self.quant

    def analisar(self):
        linha1 = f"Analisando [green]{self.titulo}[/] com [blue]{self.quant}[/] convidados"
        linha2 = f"Cada participante comerá {self.quant_carne_por_pessoa} Kg de carne e cada quilo de carne custa R${self.quilo_carne:,.2f}"
        linha3 = f"Recomendo comprar [blue]{self.carnetotal():,.2f}[/] Kg de carne"
        linha4 = f"O custo total será de [blue]R${self.precototal():,.2f}[/]"
        linha5 = f"Cada pessoa deverá colaborar com [yellow]R${self.precopessoa():,.2f}[/]"

        painel = Panel(f"{linha1}\n{linha2}\n{linha3}\n{linha4}\n{linha5}", title=self.titulo)

        print(painel)

churras = Churrasco("Churras dos amigos", 78)
churras.analisar()
