#!/usr/bin/env python3
import sys, os
import datetime
import pandas as pd
from pandas import DataFrame

base_url = "../data/processing/"
base_output_url = "../data/output/"
base_json_output_url = base_output_url + "json/"
base_excel_output_url = base_output_url + "excel/"
base_csv_output_url = base_output_url + "csv/"

def ensure_directories():
    os.makedirs(base_json_output_url, exist_ok=True)
    os.makedirs(base_excel_output_url, exist_ok=True)
    os.makedirs(base_csv_output_url, exist_ok=True)

def process_file(filename):
    file_url = base_url + filename
    print(f"Processing file {filename}")

    try:
        df = pd.read_csv(file_url)
        print(f"Loaded {len(df)} rows, {len(df.columns)} columns")
        print("First 5 rows:")
        print(df.head())

        cleaned_df = csv_cleaner(df)
        print(f"Cleaned data: {len(cleaned_df)} rows remaining")

        stats_df = calculate_stats(cleaned_df)

        convert_and_store_dataframe(stats_df, filename)
    
    except Exception as e:
        print(f"Error processing {filename}: {str(e)}")

def csv_cleaner(dataframe : DataFrame):
    print("Starting data cleaning...")

    # Remove duplicated rows
    df_without_duplicated_rows = dataframe.drop_duplicates()
    duplicates_removed = len(dataframe) - len(df_without_duplicated_rows)
    if duplicates_removed > 0:
        print(f"🗑️  Removed {duplicates_removed} duplicate rows")
    
    # Handle missing values - fill with appropriate defaults
    df_cleaned = df_without_duplicated_rows.copy()
    
    # Fill numeric columns with 0
    numeric_columns = df_cleaned.select_dtypes(include=['number']).columns
    for col in numeric_columns:
        df_cleaned[col] = df_cleaned[col].fillna(0)
    
    # Fill text columns with "Unknown" or empty string
    text_columns = df_cleaned.select_dtypes(include=['object']).columns
    for col in text_columns:
        df_cleaned[col] = df_cleaned[col].fillna("Unknown")
    
    # Clean whitespace from text columns
    for col in text_columns:
        df_cleaned[col] = df_cleaned[col].astype(str).str.strip()
    
    missing_filled = dataframe.isnull().sum().sum() - df_cleaned.isnull().sum().sum()
    if missing_filled > 0:
        print(f"🔧 Filled {missing_filled} missing values")
    
    return df_cleaned

def calculate_stats(dataframe : DataFrame):
    stats_df = { 
        "total_sales": [],
        "avg_sales": []
    }

    

def convert_and_store_dataframe(df, filename):
    ensure_directories()
    convert_to_json(df, filename)
    convert_to_excel(df, filename)
    convert_to_csv(df, filename)

def convert_to_json(data : DataFrame, filename):
    print("Generating JSON file...")
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    base_name = filename.rsplit('.', 1)[0] if '.' in filename else filename
    output_file = base_json_output_url + base_name + "_" + timestamp + ".json"
    
    data.to_json(output_file, orient='records', indent=2, force_ascii=False)
    print(f"JSON saved: {output_file}")

def convert_to_excel(data : DataFrame, filename):
    print("Generating Excel file...")
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    base_name = filename.rsplit('.', 1)[0] if '.' in filename else filename
    output_file = base_excel_output_url + base_name + "_" + timestamp + ".xlsx"
    
    data.to_excel(output_file, index=False, engine='openpyxl')
    print(f"Excel saved: {output_file}")

def convert_to_csv(data : DataFrame, filename):
    print("Generating csv file...")
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    base_name = filename.rsplit('.', 1)[0] if '.' in filename else filename
    output_file = base_csv_output_url + base_name + "_" + timestamp + ".csv"
    
    data.to_csv(output_file, index=False, encoding='utf-8')
    print(f"CSV saved: {output_file}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        process_file(filename)

    else:
        print("No file provided")
        print("Usage: python3 process_csv.py <filename>")