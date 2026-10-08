from rich import print
class Diario:
    def __init__(self, senha="CeV!@"):
        self.__senha = senha
        self.__segredos = []

    @property
    def senha(self):
        raise PermissionError("Ninguém pode ver a senha")

    def escrever(self, msg):
        self.__segredos.append(msg)

    def ler(self, senha=None):
        if senha == self.__senha:
            print("[green]Diário liberado![/]")
            for l in self.__segredos:
                print(f"- {l}")
        else:
            raise PermissionError("Senha inválida! Você não pode ler meu diário")            