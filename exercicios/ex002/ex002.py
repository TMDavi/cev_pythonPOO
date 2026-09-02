#Declaração de classe

class Gafanhoto:
    """
    Essa clase cria um gafanhoto que é uma pessoa que tem nome e idade

    Para criar uma nova pessoa,use
    variável = Gafanhoto(nome,idade)
    """

    def __init__(self, n="vazio", i=0): # Método construtor
        # Atributos de instancia
        self.nome = n
        self.idade = i

    # Métodos de instância
    def aniversario(self):
        self.idade += 1
    def mensagem(self):
        return f"{self.nome} é gafanhoto(a) e tem {self.idade} anos de idade"

    def __str__(self):
        return f"{self.nome} é gafanhoto(a) e tem {self.idade} anos de idade"

    def __getstate__(self):
        return f"Estado: nome = {self.nome} idade = {self.idade}"
# Declaração de objetos
g1 = Gafanhoto("Maria",17)
g1.aniversario()
print(g1)
print(g1.__class__)
print(g1.__dict__)
print(g1.__doc__)
print(g1.__getstate__())

g2 = Gafanhoto("Mauro",54)
print(g2.__getstate__())