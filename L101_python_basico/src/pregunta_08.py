import gzip
from pathlib import Path


def pregunta_08():
    """
    Repita la pregunta 7, pero ahora cada lista de letras debe contener cada
    letra una sola vez y estar ordenada alfabéticamente. Retorne una lista de
    tuplas `(valor, letras)` ordenada por el valor.

    Ejemplo:
        [(0, ["C"]), (1, ["B", "E"]), (2, ["A", "E"]), ...]
    """

    file_path = Path(__file__).resolve().parents[1] / "data" / "data.csv.gz"

    valores = {}

    with gzip.open(file_path, "rt", encoding="utf-8") as file:

        for linea in file:

            datos = linea.strip().split("\t")

            letra = datos[0]
            valor = int(datos[1])

            if valor not in valores:
                valores[valor] = set()

            valores[valor].add(letra)

    resultado = []

    for valor in sorted(valores):
        resultado.append(
            (valor, sorted(list(valores[valor])))
        )

    return resultado


if __name__ == "__main__":
    print(pregunta_08())