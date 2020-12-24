import re

# Completar la función regex_ayuda para que tome una expresión regular (como una cadena) y
# una cadena a la que desea aplicar la expresión regular.
# La función debe devolver una lista con todas las apariciones del patrón en la cadena.


def regex_ayuda(patron, cadena_entrada):
    pattern = re.compile(patron)
    match = pattern.match(cadena_entrada)

    return match.groups()


def main():
    print(regex_ayuda(
        r'[!?.,;:/()]', 'Este archivo tiene algunos caracteres especiales:!?.,;:/()'))


if __name__ == "__main__":
    main()
