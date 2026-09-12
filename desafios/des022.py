from rich import print
from rich.panel import Panel
from rich.traceback import install


class Controle:

    parar = 0

    tvligada = 0

    volmax = 5
    volmin = 1

    canalmax = 5
    canalmin = 1
    

    def __init__(self):
        self.volatual = 1
        self.canalatual = 1

    def subDisplayVol(self):
        if self.volatual == 1:
            return f"VOLUME: [white on blue]  [/][white on white]        [/]"
        elif self.volatual == 2:
            return f"VOLUME: [white on blue]    [/][white on white]      [/]"
        elif self.volatual == 3:
            return f"VOLUME: [white on blue]      [/][white on white]    [/]"
        elif self.volatual == 4:
            return f"VOLUME: [white on blue]        [/][white on white]  [/]"
        elif self.volatual == 5:
            return f"VOLUME: [white on blue]          [/]"

    def subDisplayCanal(self):
        if self.canalatual == 1:
            return f"CANAL: [yellow on yellow]1 [/] 2  3  4  5"
        elif self.canalatual == 2:
            return f"CANAL: 1 [yellow on yellow] 2 [/] 3  4  5"
        elif self.canalatual == 3:
            return f"CANAL: 1  2 [yellow on yellow] 3 [/] 4  5"
        elif self.canalatual == 4:
            return f"CANAL: 1  2  3 [yellow on yellow] 4 [/] 5"
        elif self.canalatual == 5:
            return f"CANAL: 1  2  3  4 [yellow on yellow] 5[/]"

    def display(self):

        if self.tvligada == 0:
            paineltv = Panel.fit(f":no_entry_sign:[red]   A TV está desligada    [/]",title="[TV]")
            print(paineltv)
        else:
            paineltv = Panel.fit(f"{self.subDisplayCanal()}\n{self.subDisplayVol()}",title="[TV]")

            print(paineltv)
            print(f" < CH{self.canalatual} >           - Vol{self.volatual} +")

    def lebotao(self, botao):
        if botao not in ["@","+","-",">","<", "0"]:
            print("[red] Opção inválida! [/]")
        
        elif botao == "0":
            self.parar = 1
        
        elif self.tvligada == 0 and botao == "@":
            self.tvligada = 1
        
        elif self.tvligada == 1 and botao == "@":
            self.tvligada = 0

        elif botao == "+":
            if self.volatual < self.volmax:
                self.volatual += 1
            else:
                pass

        elif botao == "-":
            if self.volatual > self.volmin:
                self.volatual -= 1
            else:
                pass

        elif botao == ">":
            if self.canalatual < self.canalmax:
                self.canalatual += 1
            else:
                self.canalatual = 1

        elif botao == "<":
            if self.canalatual > self.canalmin:
                self.canalatual -= 1
            else:
                self.canalatual = 5



c1 = Controle()

while not c1.parar:

    c1.display()

    botao = input()

    c1.lebotao(botao)