from rich import print
from rich import inspect

class ContaBancaria:
    """
    Cria uma conta bancaria e permite fazer saques e depósitos
    """
    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f"Conta criada com sucesso! Saldo atual de R${self.saldo:,.2f}")

    def __str__(self):
        return f"A conta {self.id} de {self.titular} tem R${self.saldo:,.2f} de saldo"

    def depositar(self,valor):
        self.saldo += valor
        print(f"Depósito de R${valor:,.2f} autorizado na conta {self.id}")

    def sacar(self, valor):
        if valor > self.saldo:
            print(f"Saque negado de valor R${valor:,.2f}: SALDO INSUFICIENTE")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:,.2f} autorizado na conta {self.id}")

c = ContaBancaria(111, "José",500)
inspect(c)