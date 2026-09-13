from rich import print
from rich.panel import Panel
from rich.traceback import install
install()

#Esse ficou quase a mesma coisa
#Alguns detalhes a mais 

class Churrasco:

    quant_carne_por_pessoa:float = 0.4
    quilo_carne:float = 82.4

    def __init__(self, titulo, quant):
        self.titulo = titulo
        self.quant = quant

    def carnetotal(self) -> float:
        return self.quant * Churrasco.quant_carne_por_pessoa

    def precototal(self) -> float:
        return self.carnetotal() * self.__class__.quilo_carne

    def precopessoa(self) -> float:
        return self.precototal() / self.quant

    def analisar(self):
        conteudo = f"Analisando [green]{self.titulo}[/] com [blue]{self.quant}[/] convidados\n"
        conteudo += f"Cada participante comerá {Churrasco.quant_carne_por_pessoa} Kg de carne e cada quilo de carne custa R${Churrasco.quilo_carne:,.2f}\n"
        conteudo += f"Recomendo comprar [blue]{self.carnetotal():,.2f} Kg[/] de carne\n"
        conteudo += f"O custo total será de [blue]R${self.precototal():,.2f}[/]\n"
        conteudo += f"Cada pessoa deverá colaborar com [yellow]R${self.precopessoa():,.2f}[/]"

        painel = Panel.fit(f"{conteudo}", title=self.titulo)

        print(painel)

churras = Churrasco("Churras dos amigos", 78)
churras.analisar()
