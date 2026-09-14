from rich import print
from rich.panel import Panel
from rich.traceback import install


class Controle:

    volmax:int = 5
    volmin:int = 1

    canalmax:int = 5
    canalmin:int = 1
    

    def __init__(self, canal = 1, vol = 1):
        self.volatual =vol
        self.canalatual = canal
        self.ligado:bool = 0

    def display(self):

        conteudo = ""
        if not self.ligado:
            conteudo += f":no_entry_sign:[red]   A TV está desligada    [/]"
            
        else:
            conteudo += f"CANAL = "
            for ch in range(Controle.canalmin, Controle.canalmax+1):
                if ch == self.canalatual:
                    conteudo += f"[black on yellow] {ch} [/]"
                else:
                    conteudo += f" {ch} "
            conteudo += f"\nVOL = "
            for vol in range(Controle.volmin, Controle.volmax+1):
                if vol <= self.volatual:
                    conteudo += f"[black on cyan]  [/]"
                else:
                    conteudo += f"[black on white]  [/]"

        painel = Panel.fit(conteudo,title="[ TV ]")
        print(painel)

    def liga_desliga(self):
        self.ligado = not self.ligado

    def canal_mais(self):
        if self.ligado:
            if self.canalatual == Controle.canalmax:
                self.canalatual = Controle.canalmin
            else:
                self.canalatual += 1

    def canal_menos(self):
        if self.ligado:
            if self.canalatual == Controle.canalmin:
                self.canalatual = Controle.canalmax
            else:
                self.canalatual -= 1

    def vol_mais(self):
        if self.ligado:
            if self.volatual != Controle.volmax:
                self.volatual += 1

    def vol_menos(self):
        if self.ligado:
            if self.volatual != Controle.volmin:
                self.volatual -= 1

c = Controle()
while True:
    c.display()
    comando = str(input(f"< CH {c.canalatual}>       - VOL{c.volatual} + "))
    match comando:
        case '0':
            break
        case "@":
            c.liga_desliga()
        case ">":
            c.canal_mais()
        case "<":
            c.canal_menos()
        case "+":
            c.vol_mais()
        case "-":
            c.vol_menos()
    print("\n"*10)
        