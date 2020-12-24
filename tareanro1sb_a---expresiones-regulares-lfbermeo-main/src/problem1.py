import re


def leer_contenido(path):
    f = open(path)
    text = f.read()
    f.close()
    return text


# Completar la función remover_puntuacion para remover las puntuaciones  !?.,;:/()
# No use iteración (bucles) en esta asignación. ¡Recuerde importar re para usar regex!
# La función debe devolver una cadena sin ninguno de los signos de puntuación anteriores.
# Sugerencia: considere usar re.sub ().
def remover_puntuacion(path_file):
    newText = re.sub(r'[!?.,;:/()]', '', leer_contenido(path_file))
    return newText


def main():
    print(remover_puntuacion("mensaje.txt"))


if __name__ == "__main__":
    main()
