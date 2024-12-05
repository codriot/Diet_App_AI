import pandas as pd
from model_training import load_model

def predict_calories(input_data):
    """Giriş verisine göre kalori tahmini yapar."""
    model = load_model()
    prediction = model.predict(pd.DataFrame([input_data]))
    return prediction[0]
