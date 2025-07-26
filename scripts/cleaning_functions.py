import pandas as pd
import numpy as np

# Load dataset
def load_data(file_path):
    return pd.read_csv(file_path)

# Remove duplicates
def remove_duplicates(df):
    before = df.shape[0]
    df_cleaned = df.drop_duplicates()
    after = df_cleaned.shape[0]
    print(f"Removed {before - after} duplicate rows.")
    return df_cleaned

# Fill missing values
def fill_missing(df):
    df['children'].fillna(0, inplace=True)
    df['country'].fillna('Unknown', inplace=True)
    df['agent'].fillna(0, inplace=True)
    df['company'].fillna(0, inplace=True)
    return df

# Remove rows with no guests
def remove_no_guests(df):
    df['total_guests'] = df['adults'] + df['children'] + df['babies']
    return df[df['total_guests'] > 0]

# Outlier removal using IQR
def remove_outliers_iqr(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    return df[(df[column] >= lower) & (df[column] <= upper)]

# Standardize categorical values
def clean_categorical(df):
    df['meal'] = df['meal'].replace('SC', 'No Meal')
    df['country'] = df['country'].str.strip().str.upper()
    return df
