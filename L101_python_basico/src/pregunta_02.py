import gzip
from pathlib import Path


def pregunta_02():
    """
    Cuente cuántos registros hay para cada letra de la primera columna
    (`letter`). Retorne una lista de tuplas `(letra, cantidad)` ordenada
    alfabéticamente por la letra.

    Ejemplo:
        [("A", 8), ("B", 7), ("C", 5)]
    """

    file_path = Path(__file__).resolve().parents[1] / "data" / "data.csv.gz"

    conteo = {}

    with gzip.open(file_path, "rt", encoding="utf-8") as file:

        for linea in file:

            datos = linea.strip().split("\t")

            letra = datos[0]

            if letra in conteo:
                conteo[letra] += 1
            else:
                conteo[letra] = 1

    return sorted(conteo.items())


if __name__ == "__main__":
    print(pregunta_02())