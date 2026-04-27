from src.data_cleaning import clean_data
from src.analysis import analyze_data
from src.reporting import generate_report

def main():
    print("\n🚀 STARTING FULL DATA PIPELINE...\n")

    # 📁 chemins des fichiers
    raw_file = "data/raw/raw_data.csv"
    clean_file = "data/processed/clean_data.csv"
    report_file = "reports/report.xlsx"

    # 🧹 1. CLEANING
    print("STEP 1: Data Cleaning...")
    df = clean_data(raw_file, clean_file)

    # 📊 2. ANALYSIS
    print("\nSTEP 2: Data Analysis...")
    analyze_data(df)

    # 📑 3. REPORTING
    print("\nSTEP 3: Report Generation...")
    generate_report(df, report_file)

    print("\n✅ PIPELINE EXECUTED SUCCESSFULLY!")
    print("📁 Clean data saved at:", clean_file)
    print("📁 Report saved at:", report_file)


# 🚀 lancement automatique
if __name__ == "__main__":
    main()