from classesex007 import Pessoa, Aluno, Professor, Funcionario
from rich import print, inspect

def main():
    a1 = Aluno("José", 17, "Informatica", "T01")
    a1.fazer_aniversario()
    a1.fazer_matricula()
    inspect(a1, methods=True)

    p1 = Professor("Samuel", 34, "Matemática", "Mestrado")
    p1.dar_aula()
    inspect(p1, methods=True)

    f1 = Funcionario("Cladia", 27, "Farmaceutico", "Farmacia")
    f1.bater_ponto()
    inspect(f1, methods=True)

    a1.estudar()
    p1.estudar( )
    f1.estudar()


if __name__ == "__main__":
    main()