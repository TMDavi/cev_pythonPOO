from rpg import *
from rich import print,inspect

def main():

    p1 = Guerreiro("Kratos", 3000)

    p2 = Mago("Gojo", 2000)

    p1.atacar(p2, 1000)

    p2.curar()

    p2.atacar(p1, 4000)
    p2.atacar(p1, 3000)


if __name__ == "__main__":
    main()