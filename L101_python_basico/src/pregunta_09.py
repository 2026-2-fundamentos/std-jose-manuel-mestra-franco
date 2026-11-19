import gzip
from pathlib import Path


def pregunta_09():
    """
    Cuente cuántas veces aparece cada clave en la quinta columna (`metrics`)
    de todo el archivo. Retorne un diccionario {clave: cantidad} con las
    claves en orden alfabético.

    Ejemplo:
        {"aaa": 13, "bbb": 16, "ccc": 23}
    """

    file_path = Path(__file__).resolve().parents[1] / "data" / "data.csv.gz"

    conteo = {}

    with gzip.open(file_path, "rt", encoding="utf-8") as file:

        for linea in file:

            datos = linea.strip().split("\t")

            pares = datos[4].split(",")

            for par in pares:

                clave = par.split(":")[0]

                if clave in conteo:
                    conteo[clave] += 1
                else:
                    conteo[clave] = 1

    resultado = {}

    for clave in sorted(conteo):
        resultado[clave] = conteo[clave]

    return resultado


if __name__ == "__main__":
    print(pregunta_09())