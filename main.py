from src.data_cleaning import clean_data

input_file = "data/raw/raw_data.csv"
output_file = "data/processed/clean_data.csv"

df = clean_data(input_file, output_file)

print(df.head())