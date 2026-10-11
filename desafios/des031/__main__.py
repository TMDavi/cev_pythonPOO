from rich import print, inspect
from retangulo import Retangulo

def main():
    r = Retangulo()
    #r.base = 3
    #r.altura = 4
    r.medidas = (12,10)
    print(r.medidas)
    inspect(r, private=True, methods=True)


if __name__ == "__main__":
    main()