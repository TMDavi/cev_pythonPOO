import hashlib
from rich import print
import getpass

class ContaBancaria:
    """
    Cria uma conta bancaria e permite fazer saques e depósitos
    """
    def __init__(self, id, nome, __saldo = 0, chave = ''):
        self._id = id 
        self._titular = nome 
        self.__saldo = __saldo 

        if chave == '':
            self.__hash = self.pede_senha()
        else:
            chave = self.gera_hash(chave)
        self.__hash = chave

        print(f"Conta criada com sucesso! Saldo atual de R${self.__saldo:,.2f}")

    def __str__(self):
        return f"Estado atual da conta: {self.__dict__}"
    #NOME
    @property
    def nome(self):
        return self._titular
    @nome.setter
    def nome(self, nome, chave=''):
        while chave == "":
            chave = self.pede_senha()
        else:
            if self.validar_senha(chave):
                self._titular = nome


    #Validação de senha
    def validar_senha(self, chave):
        hash_chave = self.gera_hash(chave)
        if hash_chave == self.__hash:
            return 1
        else:
            return 0 

    def pede_senha(self):
        senha = getpass.getpass(prompt="Digite sua senha: ", echo_char="*")
        return senha

    def gera_hash(self, valor):
        return hashlib.sha256(valor.encode("utf-8")).hexdigest()

    #deposito e saque
    def depositar(self,valor):
        valor = abs(valor)
        self.__saldo += valor
        print(f"Depósito de R${valor:,.2f} autorizado na conta {self._id}")

    def sacar(self, valor, chave=''):
        while chave == "":
            chave = self.pede_senha()
        else:
            if self.validar_senha(chave):
                valor = abs(valor)
                if valor > self.__saldo:
                    print(f"Saque negado de valor R${valor:,.2f}: saldo INSUFICIENTE")
                else:
                    self.__saldo -= valor
                    print(f"Saque de R${valor:,.2f} autorizado na conta {self._id}")
            else:
                print("[red]Senha inválida[/]")



        
