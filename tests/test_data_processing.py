# tests/test_data_processing.py
from src.data_processing import load_data, normalize_data
import os

def test_load_data():
    filepath = 'data/tips.csv'
    data = load_data(filepath)
    assert not data.empty

def test_normalize_data():
    filepath = 'data/tips.csv'
    data = load_data(filepath)
    normalized_data = normalize_data(data)
    assert normalized_data.isnull().sum().sum() == 0
