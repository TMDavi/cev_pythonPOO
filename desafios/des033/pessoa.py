from abc import ABC, abstractmethod
from rich import print
import datetime as dt

class Pessoa(ABC):
    
    def __init__(self, nome, nascimento):
        self._nome = nome
        self._nascimento = nascimento

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor) -> str:
        self._nome = valor

    @property
    def nascimento(self) -> int:
        return self._nascimento

    @nascimento.setter
    def nascimento(self, valor) -> int:
        if (valor > dt.date.today().year) or (valor < (dt.date.today().year - 130)):
            raise ValueError(f"O ano {valor} é inválido")
        else: 
            self._nascimento = valor

    @property
    def idade(self):
        return dt.date.today().year - self._nascimento

    @idade.setter
    def idade(self, valor):
        raise PermissionError("Não é possível mudar a idade. Mude o ano de Nascimento!")


class Aluno(Pessoa):
    def __init__(self, nome, nascimento, curso):
        super().__init__(nome, nascimento)
        self.cursos_oficiais = ['ADM','ADS',"ENG","CONT"]
        self._curso = curso

    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, valor):
        if valor in self.cursos_oficiais:
            self._curso = valor
        else:
            raise ValueError(f"O curso {valor} não está listado")

    def add_curso(self, valor) -> str:
        self.cursos_oficiais.append(valor)


print(dt.date.today().year)