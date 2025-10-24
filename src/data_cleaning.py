"""src/data_cleaning.py

Utility script for cleaning and preparing cricket performance datasets.
Author: Sneha Gandu
"""

import pandas as pd

def clean_dataset(df):
    """Basic cleanup: remove empty rows, trim spaces, and handle duplicates."""
    df = df.dropna(how="all")
    df = df.drop_duplicates()
    df.columns = [col.strip() for col in df.columns]
    return df

if _name_ == "_main_":
    print("This module provides basic data cleaning utilities for the project.")