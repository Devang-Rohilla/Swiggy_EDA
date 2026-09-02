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
    if column in df:
        # \D matches any character that is NOT a digit. We replace them with nothing.
        df[column] = df[column].astype(str).str.replace(r'\D', '', regex=True)
        # Convert to float (using pd.to_numeric handles empty strings better)
        df[column] = pd.to_numeric(df[column], errors='coerce')
    return df