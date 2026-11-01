from classes import *

def main():
    c1 = Carteira(1000)
    c2 = Carteira(100)
    
    if (c1 == c2):
        print("Voces tem o mesmo valor na carteira")
    else:
        print("As carteiras tem valores diferentes")
    c1 += 100

    if (c1 <= c2):
        print("A segunda carteira tem mais dinheiro")
    else:
        print("A primeira carteira tem mais dinheiro")
    print(c1)

if __name__ == "__main__":
    main()