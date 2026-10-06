from classes025 import *
from rich import print, inspect
from rich.table import Table

def main():
    dist= 5

    #Objetos
    viagens = [Moto(dist), Caminhao(dist), Drone(dist)]

    #Tabela
    tabela = Table(title="Tabela de fretes")
    tabela.add_column("Distancia", justify="left")
    tabela.add_column("Tipo", justify="left")
    tabela.add_column("Frete", justify="left")

    #Rows
    for obj in viagens:
        tabela.add_row(f"{dist}km",f"{type(obj).__name__}",f"{obj.calc_frete()}")

    print(tabela)


if __name__ == '__main__':
    main()
