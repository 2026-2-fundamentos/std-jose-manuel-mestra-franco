import gzip
from pathlib import Path


def pregunta_03():
    """
    Sume los valores de la segunda columna (`value`) para cada letra de la
    primera columna (`letter`). Retorne una lista de tuplas `(letra, suma)`
    ordenada alfabéticamente por la letra.

    Ejemplo:
        [("A", 53), ("B", 36), ("C", 27)]
    """

    file_path = Path(__file__).resolve().parents[1] / "data" / "data.csv.gz"

    suma_por_letra = {}

    with gzip.open(file_path, "rt", encoding="utf-8") as file:

        for linea in file:

            datos = linea.strip().split("\t")

            letra = datos[0]
            valor = int(datos[1])

            if letra in suma_por_letra:
                suma_por_letra[letra] += valor
            else:
                suma_por_letra[letra] = valor

    return sorted(suma_por_letra.items())


if __name__ == "__main__":
    print(pregunta_03())