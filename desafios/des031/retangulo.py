from rich import print

class Retangulo:
    
    def __init__(self, base=1, altura=1):
        self._base = None
        self._altura = None
        self._area = None

        self.base = base
        self.altura = altura
       

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, valor):
        if not isinstance(valor, float) and not isinstance(valor, int):
            raise TypeError("[red]vVALOR DEVE SER SER UM NÚMERO![/]")
        if valor< 0:
            raise ValueError("Valor inválido para altura!")
        else:
            self._base = valor
        
    
    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, valor):
        if not isinstance(valor, float) and not isinstance(valor, int):
            raise TypeError("[red]vVALOR DEVE SER SER UM NÚMERO![/]")
        if valor< 0:
            raise ValueError("Valor inválido para altura!")
        else:
            self._altura = valor

    @property
    def area(self):
        return self._altura * self._base

    @area.setter
    def area(self,valor):
        raise PermissionError("Não pode definir a área da base!")

    @property
    def medidas(self):
        #return (self._base,self._altura)
        return f'Base = {self._base}\nAltura = {self._altura}\nÁrea = {self.area}'
        
    @medidas.setter
    def medidas(self, valores:tuple):
        if not isinstance(valores, tuple):
            raise TypeError("Valores devem vir em uma tupla!")
        if len(valores) != 2:
            raise SyntaxError("Informe apenas 2 valores")
        if isinstance(valores[0], float) or isinstance(valores[0], int):
            self.base = valores[0]
        if isinstance(valores[1], float) or isinstance(valores[1], int):
            self.altura = valores[1]


