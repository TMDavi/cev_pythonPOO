from rich import print, inspect
from des030 import Credencial
import hashlib
import getpass

def main():
    c = Credencial()
    c.senha = str(getpass.getpass("Digite a senha: "))

    inspect(c, private=True, methods=True)

    #c.validar(str(getpass.getpass("Validando a senha: ")))

if __name__ == "__main__":
    main()