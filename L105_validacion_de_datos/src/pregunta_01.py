import pandas as pd
import json
import re
from pathlib import Path

def main():
    """
    Antes de limpiar o analizar un conjunto de datos, un analista debe
    documentar qué problemas tiene. En este laboratorio usted no va a limpiar
    `data/ventas.csv.gz`: va a construir un reporte de calidad que deje evidencia
    de sus problemas, tal como están en el archivo.

    Lea `data/ventas.csv.gz` sin modificar sus valores. Para trabajar con los
    encabezados, normalícelos: páselos a minúsculas, elimine los espacios al
    inicio y al final (y cualquier marca BOM) y reemplace los espacios
    internos por `_`. Las columnas requeridas son `supplier_id`, `supplier`,
    `country`, `city`, `purchase_date`, `amount`, `discount`, `weight`,
    `units`, `unit_price` y `contact_email`.

    Escriba el reporte en `submission/data_quality_report.json` con estas
    claves:

    - `row_count`: cantidad de filas de datos.
    - `column_count`: cantidad de columnas.
    - `missing_required_columns`: lista ordenada de columnas requeridas que no
      están en el archivo.
    - `unexpected_columns`: lista ordenada de columnas del archivo que no son
      requeridas.
    - `duplicate_row_count`: cantidad de filas idénticas a una fila anterior.
    - `duplicate_supplier_id_row_count`: cantidad de filas cuyo `supplier_id`
      aparece más de una vez (cuente todas esas filas, no solo las
      repetidas).
    - `missing_value_count_by_column`: diccionario con la cantidad de valores
      faltantes de cada columna. Considere faltantes las celdas vacías y las
      que contienen `N/A`.
    - `invalid_email_count`: cantidad de valores de `contact_email` que no
      tienen la forma `usuario@dominio.extension`.
    - `invalid_unit_count`: cantidad de valores numéricos de `units` que no son
      enteros positivos. Los valores faltantes no se cuentan aquí.
    - `country_values`: lista ordenada de los valores distintos de `country`,
      escritos exactamente como aparecen en el archivo.

    La función también debe retornar el reporte como un diccionario.

    Ejemplo del formato del reporte:

        {
          "row_count": 103,
          "column_count": 11,
          "missing_required_columns": [],
          ...
          "country_values": [" Colombia ", "CO", ...]
        }
    """



    file_path = (
        Path(__file__).resolve().parents[1]
        / "data"
        / "ventas.csv.gz"
    )

    df = pd.read_csv(file_path, compression="gzip")

    df.columns = (
        df.columns.astype(str)
        .str.replace("\ufeff", "", regex=False)
        .str.strip()
        .str.lower()
        .str.replace(" ", "_", regex=False)
    )

    required_columns = [
        "supplier_id",
        "supplier",
        "country",
        "city",
        "purchase_date",
        "amount",
        "discount",
        "weight",
        "units",
        "unit_price",
        "contact_email",
    ]

    missing_value_count_by_column = (
        (df.isna()) | (df == "") | (df == "N/A")
    ).sum().to_dict()

    invalid_email_count = df["contact_email"].apply(
        lambda x: (
            pd.notna(x)
            and not bool(
                re.fullmatch(
                    r"[^@\s]+@[^@\s]+\.[^@\s]+",
                    str(x),
                )
            )
        )
    ).sum()

    invalid_unit_count = df["units"].apply(
        lambda x: (
            pd.notna(x)
            and not (
                float(x).is_integer()
                and float(x) > 0
            )
        )
    ).sum()

    report = {
        "row_count": len(df),
        "column_count": len(df.columns),
        "missing_required_columns": sorted(
            [col for col in required_columns if col not in df.columns]
        ),
        "unexpected_columns": sorted(
            [col for col in df.columns if col not in required_columns]
        ),
        "duplicate_row_count": int(df.duplicated().sum()),
        "duplicate_supplier_id_row_count": int(
            df["supplier_id"].duplicated(keep=False).sum()
        ),
        "missing_value_count_by_column": {
            k: int(v)
            for k, v in missing_value_count_by_column.items()
        },
        "invalid_email_count": int(invalid_email_count),
        "invalid_unit_count": int(invalid_unit_count),
        "country_values": sorted(
            df["country"].dropna().unique().tolist()
        ),
    }

    submission_path = (
        Path(__file__).resolve().parents[1]
        / "submission"
    )

    submission_path.mkdir(exist_ok=True)

    output_file = (
        submission_path
        / "data_quality_report.json"
    )

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=2)

    return report


if __name__ == "__main__":
    print(main())
