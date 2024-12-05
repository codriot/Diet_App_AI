import numpy as np
def calculate_nutritional_score(df):
    """Besin değerlerini hesaplayan fonksiyon."""
    df['nutritional_score'] = df['protein'] * 4 + df['carbs'] * 4 + df['fats'] * 9
    return df

def add_custom_features(df):
    """Ekstra özellikler oluşturur."""
    df['is_high_protein'] = np.where(df['protein'] > 20, 1, 0)
    return df
