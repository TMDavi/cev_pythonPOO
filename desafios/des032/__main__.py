from contabancaria import ContaBancaria
from rich import print, inspect


def main():
    print('Criando a conta')
    cc = ContaBancaria('123','Davi',1000, 'cirio')

    print('Realizando depósito')
    cc.depositar(200)

    print('Realizando saque')
    cc.sacar(100,'cirio')

    cc.nome = "Manoel"

    inspect(cc, private=True, methods=True)


if __name__ == "__main__":
    main()