import pandas as pd
import numpy as np
import polars as pl  # Daha hızlı veri işleme için

def load_data(file_path):
    """Veriyi dosyadan yükler."""
    return pd.read_csv(file_path)

def clean_data(df):
    """Eksik verileri temizler ve gerekirse sütunları dönüştürür."""
    df.dropna(inplace=True)
    return df

def preprocess_data(df):
    """Özellik mühendisliği ve diğer ön işleme adımlarını gerçekleştirir."""
    df = pd.get_dummies(df, columns=['category_column'], dtype=int)
    return df
