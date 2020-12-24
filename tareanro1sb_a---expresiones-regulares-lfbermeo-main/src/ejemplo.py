import re

# Una función que devuelve una lista de palabras que se obtienen de una cadena


def obtener_palabras(cadena):
    patron = r'[a-z]+'
    regex = re.compile(patron)
    mo = regex.findall(cadena)
    return mo


def main():
    print(obtener_palabras('ejemplo de cadena'))


if __name__ == "__main__":
    main()
