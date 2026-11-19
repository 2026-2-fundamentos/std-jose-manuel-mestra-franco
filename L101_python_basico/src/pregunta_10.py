import gzip
from pathlib import Path


def pregunta_10():
    """
    Para cada registro del archivo, en el mismo orden en que aparecen,
    retorne una tupla con la letra de la primera columna (`letter`), la
    cantidad de elementos de la cuarta columna (`codes`) y la cantidad de
    pares de la quinta columna (`metrics`). El resultado es una lista con una
    tupla por registro.

    Ejemplo:
        [("E", 3, 5), ("A", 3, 4), ("B", 4, 4), ...]
    """

    file_path = Path(__file__).resolve().parents[1] / "data" / "data.csv.gz"

    resultado = []

    with gzip.open(file_path, "rt", encoding="utf-8") as file:

        for linea in file:

            datos = linea.strip().split("\t")

            letra = datos[0]

            cantidad_codes = len(datos[3].split(","))

            cantidad_metrics = len(datos[4].split(","))

            resultado.append(
                (letra, cantidad_codes, cantidad_metrics)
            )

    return resultado


if __name__ == "__main__":
    print(pregunta_10())