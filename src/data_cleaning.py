import pandas as pd

def clean_data(input_path, output_path):
    print("🔄 Loading raw data...")

    df = pd.read_csv(input_path)

    print("🧹 Cleaning data...")

    # 1. Supprimer les lignes vides
    df.dropna(inplace=True)

    # 2. Standardiser les noms de colonnes
    df.columns = df.columns.str.lower()

    # 3. Convertir les types
    df["age"] = df["age"].astype(int)
    df["montant"] = df["montant"].astype(float)

    # 4. Convertir la date
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    # 5. Supprimer les dates invalides
    df.dropna(subset=["date"], inplace=True)

    # 6. Supprimer les doublons
    df.drop_duplicates(inplace=True)

    # 7. Réinitialiser l’index
    df.reset_index(drop=True, inplace=True)

    # Sauvegarde des données propres
    df.to_csv(output_path, index=False)

    print("✅ Data cleaning completed successfully!")
    print(f"📁 Clean data saved to: {output_path}")

    return df