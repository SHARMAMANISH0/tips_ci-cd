# tests/test_model.py
from src.data_processing import load_data, normalize_data
from src.model import train_model
import os

def test_train_model():
    filepath = 'data/tips.csv'
    data = normalize_data(load_data(filepath))
    model, mse = train_model(data)
    assert model is not None
    assert mse >= 0
