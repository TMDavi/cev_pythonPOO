from rich import print, inspect
from classes_des028 import Termostato

def main():
    t1 = Termostato()

    t1.temperatura = 23
    print(f"A temperatura stual é {t1.ftemperatura}")

    inspect(t1, private=True, methods=True)

if __name__ == "__main__":
    main()