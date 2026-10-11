from rich import print

class Retangulo:
    
    def __init__(self, base=1, altura=1):
        self._base = base
        self._altura = altura
        self._area = None
       

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, valor):
        try:
            if valor > 0:
                self._base = valor
            else:
                raise ValueError("[red]Valor negativo ou zero inválido![/]")
        except TypeError:
            raise TypeError("[red]A base deve ser um número![/]")
    
    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, valor):
        try:
            if valor > 0:
                self._altura = valor
            else:
                raise ValueError("[red]Valor negativo ou zero inválido![/]")
        except TypeError:
            raise TypeError("[red]A base deve ser um número![/]")

    @property
    def area(self):
        return self._altura * self._base

    @property
    def medidas(self):
        #return (self._base,self._altura)
        return f'Base = {self._base}\nAltura = {self._altura}\nÁrea = {self.area}'
        
    @medidas.setter
    def medidas(self, tupla):
        if len(tupla) == 2:
            if tupla[0] > 0:
                self._base = tupla[0]
            if tupla[1] > 0:
                self._altura = tupla[1]
            else:
                raise ValueError("[red]Valor negativo ou zero inválido![/]")
        else:
            raise IndexError("Inserir apenas dois valores")

