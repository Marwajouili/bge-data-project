from src.data_cleaning import clean_data
from src.analysis import analyze_data
from src.reporting import generate_report

def run_pipeline():
    print("\n🚀 STARTING DATA PIPELINE...\n")

    # 📁 chemins des fichiers
    raw_path = "data/raw/raw_data.csv"
    clean_path = "data/processed/clean_data.csv"
    report_path = "reports/report.xlsx"

    # 🧹 1. CLEANING
    print("STEP 1: Cleaning data...")
    df = clean_data(raw_path, clean_path)

    # 📊 2. ANALYSIS
    print("\nSTEP 2: Analysis...")
    analyze_data(df)

    # 📑 3. REPORTING
    print("\nSTEP 3: Reporting...")
    generate_report(df, report_path)

    print("\n✅ PIPELINE COMPLETED SUCCESSFULLY!")
    print("📁 Clean data saved in:", clean_path)
    print("📁 Report saved in:", report_path)


# 🚀 lancement direct
if __name__ == "__main__":
    run_pipeline()