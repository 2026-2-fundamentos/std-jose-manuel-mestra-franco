import gzip
from pathlib import Path


def pregunta_04():
    """
    Cuente cuántos registros hay en cada mes, usando la fecha de la tercera
    columna (`date`). Represente el mes como un texto de dos dígitos y retorne
    una lista de tuplas `(mes, cantidad)` ordenada por el mes.

    Ejemplo:
        [("01", 3), ("02", 4), ("03", 2)]
    """

    file_path = Path(__file__).resolve().parents[1] / "data" / "data.csv.gz"

    conteo_meses = {}

    with gzip.open(file_path, "rt", encoding="utf-8") as file:

        for linea in file:

            datos = linea.strip().split("\t")

            fecha = datos[2]

            mes = fecha.split("-")[1]

            if mes in conteo_meses:
                conteo_meses[mes] += 1
            else:
                conteo_meses[mes] = 1

    return sorted(conteo_meses.items())


if __name__ == "__main__":
    print(pregunta_04())