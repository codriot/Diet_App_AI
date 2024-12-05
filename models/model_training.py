import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib  # Modeli kaydetmek için

def train_model(data_path):
    """Modeli eğitir ve kaydeder."""
    df = pd.read_csv(data_path)
    X = df[['carbs', 'protein', 'fats']]
    y = df['calories']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    joblib.dump(model, 'models/trained_model.pkl')
    print("Model eğitildi ve kaydedildi.")

def load_model(model_path='models/trained_model.pkl'):
    """Kaydedilen modeli yükler."""
    return joblib.load(model_path)
