from rich import print


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
        return f":handshake: Olá, sou [blue]{self.nome}[/], sou do setor de {self.setor} e estou no cargo de {self.cargo} na empresa {self.empresa}"


c1 = Funcionario("Maria", "Administração", "Diretora")
print(c1.apresentacao())

c2 = Funcionario("Pedro", "TI", "Programador")
print(c2.apresentacao())