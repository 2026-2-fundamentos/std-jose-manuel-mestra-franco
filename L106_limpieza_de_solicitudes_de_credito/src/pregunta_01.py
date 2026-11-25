
import pandas as pd
from pathlib import Path


def pregunta_01():

    file_path = (
        Path(__file__).resolve().parents[1]
        / "data"
        / "solicitudes_de_credito.csv.gz"
    )

    df = pd.read_csv(
        file_path,
        compression="gzip",
        sep=";"
    )

    print("\nCOLUMNAS ORIGINALES")
    print(df.columns.tolist())

    print("\nPRIMERAS FILAS")
    print(df.head())

    print("\nDIMENSIONES ORIGINALES")
    print(df.shape)

    print("\nCOLUMNAS ORIGINALES DETALLADAS")
    for c in df.columns:
        print(repr(c))

    df = df.loc[:, ~df.columns.astype(str).str.contains("^Unnamed")]

    df.columns = (
        df.columns.astype(str)
        .str.strip()
    )

    text_columns = [
        "sexo",
        "tipo_de_emprendimiento",
        "idea_negocio",
        "barrio",
        "línea_credito",
    ]

    for col in text_columns:
        df[col] = (
            df[col]
            .str.lower()
            .str.replace("-", " ", regex=False)
            .str.strip()
            .str.replace(r"\s+", " ", regex=True)
        )

    df["estrato"] = (
        df["estrato"]
        .astype(str)
        .str.extract(r"(\d+)")[0]
    )

    df["estrato"] = pd.to_numeric(
        df["estrato"],
        errors="coerce",
    )

    df["comuna_ciudadano"] = (
        pd.to_numeric(
            df["comuna_ciudadano"],
            errors="coerce"
        )
        .round()
        .astype("Int64")
    )

    df["monto_del_credito"] = (
        df["monto_del_credito"]
        .astype(str)
        .str.replace(r"[^0-9]", "", regex=True)
    )

    df["monto_del_credito"] = pd.to_numeric(
        df["monto_del_credito"],
        errors="coerce",
    )

    fechas = pd.to_datetime(
        df["fecha_de_beneficio"],
        format="%d/%m/%Y",
        errors="coerce"
    )

    fechas = fechas.fillna(
        pd.to_datetime(
            df["fecha_de_beneficio"],
            format="%Y/%m/%d",
            errors="coerce"
        )
    )

    fechas = fechas.fillna(
        pd.to_datetime(
            df["fecha_de_beneficio"],
            format="%Y-%m-%d",
            errors="coerce"
        )
    )

    df["fecha_de_beneficio"] = fechas.dt.strftime("%Y-%m-%d")

    columnas_requeridas = [
        "sexo",
        "tipo_de_emprendimiento",
        "idea_negocio",
        "barrio",
        "estrato",
        "fecha_de_beneficio",
        "monto_del_credito",
        "línea_credito",
    ]

    print("\nVALORES VACÍOS COMO TEXTO")

    for col in text_columns:
        print(col)
        print(df[col].isin(["", " ", "nan"]).sum())

    print("\nESTRATOS ORIGINALES")
    print(df["estrato"].astype(str).value_counts().head(30))

    # Reemplazar textos vacíos por valores nulos
    df["barrio"] = df["barrio"].replace("", pd.NA)
    df["idea_negocio"] = df["idea_negocio"].replace("", pd.NA)

    # Eliminar registros incompletos
    df = df.dropna(subset=columnas_requeridas)

    df["estrato"] = df["estrato"].astype("Int64")
    df["monto_del_credito"] = df["monto_del_credito"].astype("Int64")
    df["comuna_ciudadano"] = df["comuna_ciudadano"].astype("Int64")

    print("\n" + "=" * 70)
    print("DIAGNOSTICO ANTES DE ELIMINAR DUPLICADOS")
    print("=" * 70)

    print("\nFILAS ACTUALES:")
    print(len(df))

    print("\nNULOS POR COLUMNA:")
    print(df.isna().sum())

    print("\nSEXO:")
    print(df["sexo"].value_counts())

    print("\nTIPO:")
    print(df["tipo_de_emprendimiento"].value_counts())

    print("\nIDEAS UNICAS:")
    print(df["idea_negocio"].nunique())

    print("\nTOP 20 IDEAS:")
    print(df["idea_negocio"].value_counts().head(20))

    print("\nBARRIOS UNICOS:")
    print(df["barrio"].nunique())

    print("\nTOP 20 BARRIOS:")
    print(df["barrio"].value_counts().head(20))

    print("\nESTRATO:")
    print(df["estrato"].value_counts().sort_index())

    print("\nCOMUNA:")
    print(df["comuna_ciudadano"].value_counts(dropna=False).sort_index())

    print("\nLINEA DE CREDITO:")
    print(df["línea_credito"].value_counts())

    # Diagnóstico de duplicados ignorando comuna
    cols = [
        "sexo",
        "tipo_de_emprendimiento",
        "idea_negocio",
        "barrio",
        "estrato",
        "fecha_de_beneficio",
        "monto_del_credito",
        "línea_credito",
    ]

    print("\nDUPLICADOS POR TODAS LAS COLUMNAS EXCEPTO COMUNA")
    print(df.duplicated(subset=cols).sum())

    print("\nDUPLICADOS EXACTOS")
    print(df.duplicated().sum())

    print("\nPRIMEROS DUPLICADOS EXACTOS")
    print(df[df.duplicated(keep=False)].head(30))

    # Normalización adicional de caracteres y acentos
    for col in text_columns:
        df[col] = (
            df[col]
            .str.normalize("NFKD")
            .str.encode("ascii", errors="ignore")
            .str.decode("utf-8")
        )

    print("\nDUPLICADOS DESPUÉS DE NORMALIZAR ACENTOS")
    print(df.duplicated().sum())

    print("\nDUPLICADOS IGNORANDO COMUNA DESPUÉS DE NORMALIZAR")
    print(df.duplicated(subset=cols).sum())

    # Eliminar duplicados exactos
    df = df.drop_duplicates(
    subset=[
        "sexo",
        "tipo_de_emprendimiento",
        "idea_negocio",
        "barrio",
        "estrato",
        "fecha_de_beneficio",
        "monto_del_credito",
        "línea_credito",
    ]
)

    # NUEVOS DIAGNÓSTICOS SOLICITADOS POR COPILOT
    print("\n" + "=" * 70)
    print("RESULTADOS FINALES PARA COMPARAR CON EL TEST")
    print("=" * 70)

    print("\nFILAS DESPUÉS:")
    print(len(df))

    print("\nSEXO:")
    print(df["sexo"].value_counts().to_dict())

    print("\nTIPO:")
    print(df["tipo_de_emprendimiento"].value_counts().to_dict())

    print("\nESTRATO:")
    print(df["estrato"].value_counts().sort_index().to_dict())

    print("\nLINEA:")
    print(df["línea_credito"].value_counts().to_dict())

    print("\nCOMUNA NULA:")
    print(df["comuna_ciudadano"].isna().sum())

    print("\nFECHAS NULAS:")
    print(df["fecha_de_beneficio"].isna().sum())

    print("\nESTRATOS UNICOS:")
    print(sorted(df["estrato"].unique()))

    # Preparar tipos finales
    df["estrato"] = df["estrato"].astype(int)
    df["monto_del_credito"] = df["monto_del_credito"].astype(int)

    # Seleccionar columnas requeridas
    df = df[
        [
            "sexo",
            "tipo_de_emprendimiento",
            "idea_negocio",
            "barrio",
            "estrato",
            "comuna_ciudadano",
            "fecha_de_beneficio",
            "monto_del_credito",
            "línea_credito",
        ]
    ]

    # Exportar archivo
    output_dir = (
        Path(__file__).resolve().parents[1]
        / "submission"
    )

    output_dir.mkdir(exist_ok=True)

    output_file = output_dir / "solicitudes_de_credito.csv"

    df.to_csv(
        output_file,
        sep=";",
        index=False
    )

    return df


if __name__ == "__main__":
    pregunta_01()
