import pandas as pd
from pathlib import Path

def pregunta_01():
    """
    ¿Cuántos registros tiene la tabla `data/tbl0.tsv`? Retorne la cantidad
    como un número entero.

    Ejemplo del formato de la respuesta:

        40
    """
    file_path = Path(__file__).resolve().parents[1] / "data" / "tbl0.tsv"

    df = pd.read_csv(file_path, sep="\t")

    return len(df)

if __name__ == "__main__":
    print(pregunta_01())