from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel

class Funcionario(ABC):

    sal_min = 1612
    inss = 0.075

    def __init__(self, nome, sal_bruto=0, salario=0):
        self.nome = nome
        self.sal_bruto = sal_bruto
        self.salario = salario
        

    @abstractmethod
    def calc_sal(self):
        pass

    def analisar_sal(self):
        analise = Panel.fit(f"O salário de [blue]{self.nome}[/] ([purple]{self.__class__.__name__}[/]) é de [green]R${self.salario:.2f}[/] \ne corresponde a [yellow]{(self.salario/Funcionario.sal_min):.1f} salários mínimos[/]", title = "Análise de Salário")

        print(analise)

class Horista(Funcionario):
    def __init__(self, nome, valor_hora, horas_trab, sal_bruto=0, salario=0):
        super().__init__(nome, salario, sal_bruto)
        self.valor_hora = valor_hora
        self.horas_trab = horas_trab

    def calc_sal(self):
        self.sal_bruto = self.horas_trab * self.valor_hora
        self.salario = self.sal_bruto - (self.sal_bruto * Funcionario.inss)

        return self.salario

class Mensalista(Funcionario):

    def __init__(self, nome, sal_bruto=0,salario=0):
        super().__init__(nome, salario, sal_bruto)

    def calc_sal():
        self.salario = self.sal_bruto - (self.sal_bruto * Funcionario.inss)
        return self.salario