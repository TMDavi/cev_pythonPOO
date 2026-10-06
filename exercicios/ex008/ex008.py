class ContaBancaria:
    """
    Cria uma conta bancaria e permite fazer saques e depósitos
    """
    def __init__(self, id, nome, __saldo = 0):
        self.id = id #Publico
        self._titular = nome #Protegido
        self.__saldo = __saldo #Privado
        print(f"Conta criada com sucesso! __saldo atual de R${self.__saldo:,.2f}")

    def __str__(self):
        return f"Estado atual da conta: {self.__dict__}"

    def depositar(self,valor):
        valor = abs(valor)
        self.__saldo += valor
        print(f"Depósito de R${valor:,.2f} autorizado na conta {self.id}")

    def sacar(self, valor):
        valor = abs(valor)
        if valor > self.__saldo:
            print(f"Saque negado de valor R${valor:,.2f}: __saldo INSUFICIENTE")
        else:
            self.__saldo -= valor
            print(f"Saque de R${valor:,.2f} autorizado na conta {self.id}")


