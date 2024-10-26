# src/data_processing.py
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def load_data(filepath):
    return pd.read_csv(filepath)

def normalize_data(df):
    scaler = MinMaxScaler()
    numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
    df[numerical_cols] = scaler.fit_transform(df[numerical_cols])
    return df
