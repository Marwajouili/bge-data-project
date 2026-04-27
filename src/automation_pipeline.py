from src.data_cleaning import clean_data
from src.analysis import analyze_data
from src.reporting import generate_report

def run_pipeline():
    raw_path = "data/raw/raw_data.csv"
    clean_path = "data/processed/clean_data.csv"
    report_path = "reports/report.xlsx"

    df = clean_data(raw_path, clean_path)
    analyze_data(df)
    generate_report(df, report_path)

    print("\n🚀 Pipeline completed successfully")