import pandas as pd
import re
from pathlib import Path


def pregunta_01():
    """
    Convierte el archivo clusters_report.txt en un DataFrame.
    """

    file_path = (
        Path(__file__).resolve().parents[1]
        / "data"
        / "clusters_report.txt"
    )

    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    patron = re.compile(
        r"^\s*(\d+)\s+(\d+)\s+([\d,]+)\s+%\s+(.*)$"
    )

    datos = []

    cluster = None
    cantidad = None
    porcentaje = None
    palabras = ""

    for line in lines:

        match = patron.match(line)

        if match:

            if cluster is not None:

                palabras = re.sub(r"\s+", " ", palabras)
                palabras = re.sub(r"\s*,\s*", ", ", palabras)
                palabras = palabras.strip(" ,.")

                datos.append(
                    {
                        "cluster": cluster,
                        "cantidad_de_palabras_clave": cantidad,
                        "porcentaje_de_palabras_clave": porcentaje,
                        "principales_palabras_clave": palabras,
                    }
                )

            cluster = int(match.group(1))
            cantidad = int(match.group(2))
            porcentaje = float(match.group(3).replace(",", "."))

            palabras = match.group(4).strip()

        elif cluster is not None:

            texto = line.strip()

            if texto and not texto.startswith("-"):
                palabras += " " + texto

    if cluster is not None:

        palabras = re.sub(r"\s+", " ", palabras)
        palabras = re.sub(r"\s*,\s*", ", ", palabras)
        palabras = palabras.strip(" ,.")

        datos.append(
            {
                "cluster": cluster,
                "cantidad_de_palabras_clave": cantidad,
                "porcentaje_de_palabras_clave": porcentaje,
                "principales_palabras_clave": palabras,
            }
        )

    return pd.DataFrame(datos)


if __name__ == "__main__":
    print(pregunta_01())