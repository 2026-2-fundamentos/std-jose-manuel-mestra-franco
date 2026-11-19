import gzip
from pathlib import Path

def pregunta_01():
    """
    Calcule la suma de los valores de la segunda columna (`value`) del
    archivo `data/data.csv.gz` y retorne el resultado como un número entero.

    Ejemplo del formato de la respuesta:

        214
    """
    file_path = Path(__file__).resolve().parents[1] / "data" / "data.csv.gz"

    suma = 0

    with gzip.open(file_path, "rt", encoding="utf-8") as file:

        for linea in file:

            datos = linea.strip().split("\t")

            suma += int(datos[1])

    return suma


if __name__ == "__main__":
    print(pregunta_01())