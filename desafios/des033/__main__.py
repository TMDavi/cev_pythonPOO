from rich import print, inspect
from pessoa import Pessoa, Aluno

def main():
    a1 = Aluno('Maria',2000,'ADM')
    
    a1.add_curso("MODA")
    a1.curso = "MODA"
    inspect(a1, private=True, methods=True)


if __name__ == "__main__":
    main()



