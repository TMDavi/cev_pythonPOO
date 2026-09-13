from rich import print
from rich import inspect

class Funcionario:
    """
    Crie a classe funcionário onde podemos cadastrar nome setor e cargo. Crie também um étodo que permita o funcionário se apresentar.
    """
    empresa = "Curso em video"

    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
        
    def apresentacao(self):
        return f":handshake: Olá, sou [blue]{self.nome}[/], sou do setor de {self.setor} e estou no cargo de {self.cargo} na empresa {Funcionario.empresa}"


c1 = Funcionario("Maria", "Administração", "Diretora")
#c1.empresa = "Estudonauta"
print(c1.apresentacao())
#print(inspect(c1))

c2 = Funcionario("Pedro", "TI", "Programador")
print(c2.apresentacao())