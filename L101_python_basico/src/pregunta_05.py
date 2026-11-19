import gzip
from pathlib import Path


def pregunta_05():
    """
    Para cada letra de la primera columna (`letter`), encuentre el valor
    máximo y el valor mínimo de la segunda columna (`value`). Retorne una lista
    de tuplas `(letra, máximo, mínimo)` ordenada alfabéticamente por la letra.

    Ejemplo:
        [("A", 9, 2), ("B", 9, 1), ...]
    """

    file_path = Path(__file__).resolve().parents[1] / "data" / "data.csv.gz"

    datos_letra = {}

    with gzip.open(file_path, "rt", encoding="utf-8") as file:

        for linea in file:

            datos = linea.strip().split("\t")

            letra = datos[0]
            valor = int(datos[1])

            if letra not in datos_letra:
                datos_letra[letra] = [valor, valor]
            else:
                if valor > datos_letra[letra][0]:
                    datos_letra[letra][0] = valor

                if valor < datos_letra[letra][1]:
                    datos_letra[letra][1] = valor

    resultado = []

    for letra in sorted(datos_letra):
        resultado.append(
            (letra, datos_letra[letra][0], datos_letra[letra][1])
        )

    return resultado


if __name__ == "__main__":
    print(pregunta_05())