import pandas as pd

def generate_report(df, output_path):
    report = df.groupby("type_projet")["montant"].sum().reset_index()

    report.to_excel(output_path, index=False)

    print("✔ Report generated:", output_path)