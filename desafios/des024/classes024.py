from abc import ABC, abstractmethod

class BebidaQuente(ABC):

    def __init__(self):
        pass
    
    def preparar(self):
        
        print(
        f"""
        --- Iniciando o Preparo ---
        {self.ferver_agua()}
        {self.misturar()}
        {self.servir()}
        --- Bebida Pronta ---
        """
        )

    def ferver_agua(self):
        return "1. Fervendo água a 100 graus Celsius."

    @abstractmethod
    def misturar(self):
        pass
        
    @abstractmethod
    def servir(self):
        pass

class Cafe(BebidaQuente):
    def __init__(self):
        super().__init__()

    def misturar(self):
        return "2. Passando água pressurizada pelo pó de café moido."

    def servir(self):
        return "3. Servindo em xícara pequena"

class Cha(BebidaQuente):
    def __init__(self):
        super().__init__()

    def misturar(self):
        return "2. Mergulhando o sachê de ervas na água"

    def servir(self):
        return "3. Servindo na caneca de porcelana com limão"

class Leite(BebidaQuente):
    def __init__(self):
        super().__init__()

    def misturar(self):
        return "2. Passando vapor pressurizado pelo bico do leite"

    def servir(self):
        return "3. Servndo na caneca grande, já com café"