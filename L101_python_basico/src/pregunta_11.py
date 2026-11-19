import gzip
from pathlib import Path


def pregunta_11():
    """
    La cuarta columna (`codes`) contiene letras minúsculas separadas por
    comas. Para cada una de esas letras, sume los valores de la segunda
    columna (`value`) de los registros en los que aparece. Retorne un
    diccionario `{letra: suma}` con las letras en orden alfabético.

    Ejemplo:
        {"a": 122, "b": 49, "c": 91}
    """

    file_path = Path(__file__).resolve().parents[1] / "data" / "data.csv.gz"

    sumas = {}

    with gzip.open(file_path, "rt", encoding="utf-8") as file:

        for linea in file:

            datos = linea.strip().split("\t")

            valor = int(datos[1])

            letras = datos[3].split(",")

            for letra in letras:

                if letra in sumas:
                    sumas[letra] += valor
                else:
                    sumas[letra] = valor

    resultado = {}

    for letra in sorted(sumas):
        resultado[letra] = sumas[letra]

    return resultado


if __name__ == "__main__":
    print(pregunta_11())