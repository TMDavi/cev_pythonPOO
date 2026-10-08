from diario import Diario
from rich import inspect, print

def main():
    d = Diario()

    d.escrever("Olá")
    d.escrever("Estou aprendendo POO em python")
    d.escrever("Espero me tornar um programador um dia")

    d.ler("CeV!@")

    inspect(d, private=True, methods=True)

if __name__ == "__main__":
    main()