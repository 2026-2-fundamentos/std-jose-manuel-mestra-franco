import gzip
from pathlib import Path


def pregunta_06():
    """
    La quinta columna (`metrics`) contiene pares `clave:valor` separados por
    comas. Para cada clave, encuentre el valor mínimo y el valor máximo que
    aparecen en todo el archivo. Retorne una lista de tuplas
    `(clave, mínimo, máximo)` ordenada alfabéticamente por la clave.

    Ejemplo:
        [("aaa", 1, 9), ("bbb", 1, 9), ...]
    """

    file_path = Path(__file__).resolve().parents[1] / "data" / "data.csv.gz"

    metricas = {}

    with gzip.open(file_path, "rt", encoding="utf-8") as file:

        for linea in file:

            datos = linea.strip().split("\t")

            pares = datos[4].split(",")

            for par in pares:

                clave, valor = par.split(":")
                valor = int(valor)

                if clave not in metricas:
                    metricas[clave] = [valor, valor]
                else:

                    if valor < metricas[clave][0]:
                        metricas[clave][0] = valor

                    if valor > metricas[clave][1]:
                        metricas[clave][1] = valor

    resultado = []

    for clave in sorted(metricas):
        resultado.append(
            (clave, metricas[clave][0], metricas[clave][1])
        )

    return resultado


if __name__ == "__main__":
    print(pregunta_06())