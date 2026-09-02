import pandas as pd 
import numpy as np 
def clean_column_names(df):
    # Converts the uppercase letter to lower and removes the blank spaces etc
    df.columns = df.columns.str.lower().str.strip().str.replace(" ","_")
    return df
def clean_rating_column(df, col_name='rating'):
    """Converts string ratings to float and forces invalid entries ('--') to NaN."""
    if col_name in df.columns:
        df[col_name] = pd.to_numeric(df[col_name], errors='coerce')
    return df
def clean_rating_count(df,col_name='rating_count'):
    #This function converts the rating_count from string to numeric
    if col_name in df.columns:
        # The r'(\d+)' regex extracts the first sequence of digits it finds in the string
        df[col_name] = df[col_name].astype(str).str.extract(r'(\d+)').astype(float)
    return df
def cost_str_to_float(df, column='cost'):
    if column in df.columns:
        # 1. Extract the first valid number sequence (e.g., '250' from '₹250 FOR 2' or '1,250')
        extracted_str = df[column].astype(str).str.extract(r'([\d,]+)', expand=False)
        
        # 2. Remove commas from the extracted string
        clean_str = extracted_str.str.replace(',', '', regex=False)
        
        # 3. Convert to float, coercing any remaining errors to NaN
        df[column] = pd.to_numeric(clean_str, errors='coerce')
        
    return df