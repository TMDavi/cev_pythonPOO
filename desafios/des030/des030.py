import hashlib
from rich import print

class Credencial:
    def __init__(self):
        self.__hash = ''

    @property
    def senha(self):
        return self.__hash

    @senha.setter
    def senha(self, valor):
        self.__hash = self.gera_hash(valor)

    def gera_hash(self, valor):
        return hashlib.sha256(valor.encode("utf-8")).hexdigest()

    def validar(self, chave):
        hash_senha = self.__hash
        hash_chave = self.gera_hash(chave)

        if hash_senha == hash_chave:
            print("[green]Senha correta![/]")
        else:
            print("[red]Senha não bate![/]")
            
