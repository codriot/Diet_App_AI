import pandas as pd
import json
from sklearn.neighbors import NearestNeighbors
import joblib

# Verilerin yüklenmesi
data = pd.read_csv('./Data/raw_data/recipes.csv')

# Modeli ve scaler'ı yükleme
knn = joblib.load('./model/model_training.pkl')
scaler = joblib.load('./model/scaler.pkl')

# Özelliklerin seçilmesi ve ölçeklendirilmesi
features = ['Calories', 'ProteinContent', 'CarbohydrateContent', 'FatContent']
X = data[features]
X_scaled = scaler.transform(X)

# Öneri fonksiyonu
def recommend_recipes(recipe_index, n_recommendations=5):
    distances, indices = knn.kneighbors([X_scaled[recipe_index]])
    recommendations = data.iloc[indices[0]]
    return recommendations

# "Turkish" anahtar kelimesine sahip tarifleri ayırma ve JSON formatında döndürme
def get_turkish_recipes_json():
    turkish_recipes = []
    for i in range(len(data)):
        recommendations = recommend_recipes(i)
        turkish_recipes.extend(recommendations[recommendations['Keywords'].str.contains('Turkish', na=False)]['Name'].tolist())
    turkish_recipes = list(set(turkish_recipes))  # Benzersiz tarif isimlerini tutma
    return json.dumps(turkish_recipes, ensure_ascii=False)

# Türk tariflerinin isimlerini JSON formatında döndürme
turkish_recipe_names_json = get_turkish_recipes_json()
print(turkish_recipe_names_json)