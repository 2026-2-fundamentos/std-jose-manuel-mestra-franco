import gzip
from pathlib import Path


def pregunta_07():
    """
    Para cada valor distinto de la segunda columna (`value`), construya la
    lista de letras de la primera columna (`letter`) que aparecen con ese
    valor. Conserve las letras repetidas y el orden en que aparecen en el
    archivo. Retorne una lista de tuplas `(valor, letras)` ordenada por el
    valor.
    """

    file_path = Path(__file__).resolve().parents[1] / "data" / "data.csv.gz"

    valores = {}

    with gzip.open(file_path, "rt", encoding="utf-8") as file:

        for linea in file:

            datos = linea.strip().split("\t")

            letra = datos[0]
            valor = int(datos[1])

            if valor not in valores:
                valores[valor] = []

            valores[valor].append(letra)

    return sorted(valores.items())


if __name__ == "__main__":
    print(pregunta_07())