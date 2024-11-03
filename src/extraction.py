import os
import pandas as pd

def load_data():
    base_path = os.path.dirname(__file__)  # Pega o caminho do arquivo `extraction.py`
    file_path = os.path.join(base_path, '..', 'data', 'bikes_completed.csv')  # Caminho relativo à pasta `src`
    return pd.read_csv(file_path)
