from ex010 import *
from rich import print, inspect

def main():
    av1 = Avaliacao("Pedro", "Matematica", 9.5)
    av1.nota = 8.9
    print(f"{av1.nome} tirou {av1.nota} em {av1.disciplina}")
    inspect(av1)

if __name__ == "__main__":
    main()