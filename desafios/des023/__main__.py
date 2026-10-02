from rich import print, inspect
from classes023 import Poligono, Quadrado, Circulo

def main():
    q1 = Quadrado(12)

    print(f'Perímetro = {q1.perimetro():.1f}')
    print(f'Area = {q1.area():.1f}')

    c1 = Circulo(20)

    print(f'Perímetro = {c1.perimetro():.1f}')
    print(f'Area = {c1.area():.1f}')



if __name__ == '__main__':
    main()