import gzip
from pathlib import Path


def pregunta_12():
    """
    Para cada letra de la primera columna (`letter`), sume todos los valores
    numéricos de los pares `clave:valor` de la quinta columna (`metrics`).
    Retorne un diccionario `{letra: suma}` con las letras en orden alfabético.

    Ejemplo:
        {"A": 177, "B": 187, "C": 114}
    """

    file_path = Path(__file__).resolve().parents[1] / "data" / "data.csv.gz"

    sumas = {}

    with gzip.open(file_path, "rt", encoding="utf-8") as file:

        for linea in file:

            datos = linea.strip().split("\t")

            letra = datos[0]

            total_fila = 0

            pares = datos[4].split(",")

            for par in pares:

                valor = int(par.split(":")[1])

                total_fila += valor

            if letra in sumas:
                sumas[letra] += total_fila
            else:
                sumas[letra] = total_fila

    resultado = {}

    for letra in sorted(sumas):
        resultado[letra] = sumas[letra]

    return resultado


if __name__ == "__main__":
    print(pregunta_12())