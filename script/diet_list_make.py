import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt
import seaborn as sns

# Verilerin yüklenmesi
data = pd.read_csv('./Data/raw_data/recipes.csv')

# Sütun adlarını kontrol etme
print(data.columns)

# Verilerin temizlenmesi
data.dropna(inplace=True)
data['RecipeServings'] = pd.to_numeric(data['RecipeServings'], errors='coerce')
data.dropna(inplace=True)

# Özelliklerin seçilmesi ve ölçeklendirilmesi
features = ['Calories', 'ProteinContent', 'CarbohydrateContent', 'FatContent']
X = data[features]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Modelin eğitilmesi
knn = NearestNeighbors(n_neighbors=5)
knn.fit(X_scaled)

# Öneri fonksiyonu
def recommend_recipes(recipe_index, n_recommendations=5):
    distances, indices = knn.kneighbors([X_scaled[recipe_index]])
    recommendations = data.iloc[indices[0]]
    return recommendations

# Örnek öneri
print(recommend_recipes(0))

# Diyet listesi oluşturma fonksiyonu
def create_diet_list(calorie_limit):
    diet_list = []
    total_calories = 0
    for i in range(len(data)):
        if total_calories >= calorie_limit:
            break
        recommendations = recommend_recipes(i)
        for _, recipe in recommendations.iterrows():
            if total_calories + recipe['Calories'] <= calorie_limit:
                diet_list.append(recipe)
                total_calories += recipe['Calories']
    return pd.DataFrame(diet_list)

# Örnek diyet listesi oluşturma
calorie_limit = 2000
diet_list = create_diet_list(calorie_limit)
print(diet_list)

# Diyet listesini CSV dosyasına kaydetme
diet_list.to_csv('./Data/processed_data/diet_list3.csv', index=False)