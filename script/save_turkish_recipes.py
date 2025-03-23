# import pandas as pd

# # Verilerin yüklenmesi
# data = pd.read_csv('./Data/raw_data/recipes.csv')

# # Sadece "Turkish" anahtar kelimesine sahip tarifleri ayırma
# turkish_recipes = data[data['Keywords'].str.contains('Turkish', na=False)]

# # Türk tariflerini CSV dosyasına kaydetme
# turkish_recipes.to_csv('./Data/processed_data/turkish_food.csv', index=False)
# import pandas as pd

# # Verilerin yüklenmesi
# data = pd.read_csv('./Data/raw_data/recipes.csv')

# # Sadece "Turkish" anahtar kelimesine sahip tarifleri ayırma
# turkish_recipes = data[data['Keywords'].str.contains('Turkish', na=False)]

# # Türk tariflerinin isimlerini JSON formatında yazdırma
# turkish_recipe_names = turkish_recipes['Name'].tolist()
# print(turkish_recipe_names)
import pandas as pd
import json

# Verilerin yüklenmesi
data = pd.read_csv('./Data/raw_data/recipes.csv')

# Sadece "Turkish" anahtar kelimesine sahip tarifleri ayırma
turkish_recipes = data[data['Keywords'].str.contains('Turkish', na=False)]

# Türk tariflerinin isimlerini JSON formatında döndürme
turkish_recipe_names = turkish_recipes['Name'].tolist()
turkish_recipe_names_json = json.dumps(turkish_recipe_names, ensure_ascii=False)
print(turkish_recipe_names_json)

