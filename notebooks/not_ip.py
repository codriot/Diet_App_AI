# Gerekli kütüphanelerin içe aktarılması
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pylab 
import scipy.stats as stats
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer

# Verilerin yüklenmesi
data = pd.read_csv('../Data/raw_data/recipes.csv')
data.head()  # İlk birkaç satırın görüntülenmesi

# Verilerin keşfi
data.info()  # Veri çerçevesinin genel bilgileri
data.shape  # Veri çerçevesinin boyutları
data.describe()  # Sayısal sütunların özet istatistikleri
data.nunique()  # Her sütundaki benzersiz değerlerin sayısı
data.isnull().sum()  # Her sütundaki eksik değerlerin sayısı
(data.isnull().sum()/(len(data)))*100  # Eksik değerlerin yüzdesi

# Verilerin temizlenmesi
copy_data = data.copy()  # Veri çerçevesinin kopyalanması
copy_data.RecipeServings = pd.to_numeric(copy_data.RecipeServings, errors='coerce')  # RecipeServings sütununun sayısal değerlere dönüştürülmesi
copy_data.dropna(how='any', inplace=True)  # Eksik değerler içeren satırların kaldırılması

# Histogram ve normallik grafiği oluşturma
fig, ax = plt.subplots(figsize=(10, 8))  # Grafik boyutlarını ayarlama
plt.title('Frequency Histogram')  # Grafik başlığı
plt.ylabel('Frequency')  # Y ekseni etiketi
plt.xlabel('Bins Center')  # X ekseni etiketi
# Histogram oluşturma, kalorileri belirli aralıklara (bins) bölerek frekanslarını gösterme
ax.hist(data.Calories.to_numpy(), bins=[0,100,200,300,400,500,600,700,800,900,1000,1000,2000,3000,5000], linewidth=0.5, edgecolor="white")
plt.show()  # Grafiği gösterme

# Normallik grafiği oluşturma, verilerin normal dağılıma ne kadar uyduğunu kontrol etme
stats.probplot(data.Calories.to_numpy(), dist="norm", plot=pylab)
pylab.show()

# Model eğitimi
scaler = StandardScaler()  # Verileri ölçeklendirmek için StandardScaler kullanma
# Verileri ölçeklendirme, belirli sütunları seçerek
prep_data = scaler.fit_transform(extracted_data.iloc[:,6:15].to_numpy())

# NearestNeighbors modelini oluşturma ve eğitme
neigh = NearestNeighbors(metric='cosine', algorithm='brute')
neigh.fit(prep_data)

# Pipeline oluşturma
# NearestNeighbors modelini pipeline'a eklemek için FunctionTransformer kullanma
transformer = FunctionTransformer(neigh.kneighbors, kw_args={'return_distance':False})
# Pipeline oluşturma, önce verileri ölçeklendirme, sonra NearestNeighbors modelini uygulama
pipeline = Pipeline([('std_scaler', scaler), ('NN', transformer)])

# Fonksiyonlar
def scaling(dataframe):
    # Verileri ölçeklendirme fonksiyonu
    scaler = StandardScaler()
    prep_data = scaler.fit_transform(dataframe.iloc[:,6:15].to_numpy())
    return prep_data, scaler

def nn_predictor(prep_data):
    # NearestNeighbors modelini oluşturma ve eğitme fonksiyonu
    neigh = NearestNeighbors(metric='cosine', algorithm='brute')
    neigh.fit(prep_data)
    return neigh

def build_pipeline(neigh, scaler, params):
    # Pipeline oluşturma fonksiyonu
    transformer = FunctionTransformer(neigh.kneighbors, kw_args=params)
    pipeline = Pipeline([('std_scaler', scaler), ('NN', transformer)])
    return pipeline

def extract_data(dataframe, ingredient_filter, max_nutritional_values):
    # Verileri filtreleme ve belirli besin değerlerine göre ayıklama fonksiyonu
    extracted_data = dataframe.copy()
    for column, maximum in zip(extracted_data.columns[6:15], max_nutritional_values):
        extracted_data = extracted_data[extracted_data[column] < maximum]
    if ingredient_filter != None:
        for ingredient in ingredient_filter:
            extracted_data = extracted_data[extracted_data['RecipeIngredientParts'].str.contains(ingredient, regex=False)]
    return extracted_data

def apply_pipeline(pipeline, _input, extracted_data):
    # Pipeline'ı uygulama ve önerilen tarifleri döndürme fonksiyonu
    return extracted_data.iloc[pipeline.transform(_input)[0]]

def recommand(dataframe, _input, max_nutritional_values, ingredient_filter=None, params={'return_distance':False}):
    # Öneri fonksiyonu, verileri ayıklama, ölçeklendirme, model oluşturma ve pipeline'ı uygulama
    extracted_data = extract_data(dataframe, ingredient_filter, max_nutritional_values)
    prep_data, scaler = scaling(extracted_data)
    neigh = nn_predictor(prep_data)
    pipeline = build_pipeline(neigh, scaler, params)
    return apply_pipeline(pipeline, _input, extracted_data)

# Öneri fonksiyonunun kullanımı
test_input = extracted_data.iloc[0:1,6:15].to_numpy()  # Test verisi oluşturma
recommand(dataset, test_input, max_list)  # Öneri fonksiyonunu çağırma

# Verilerin kaydedilmesi
dataset.to_csv('dataset.csv', index=False)  # Verileri CSV dosyasına kaydetme
dataset.to_json('dataset.json')  # Verileri JSON dosyasına kaydetme

# Kaloriye göre öneri fonksiyonu
def recommend_by_calories(dataframe, max_daily_fat, max_nutritional_values, ingredient_filter=None, params={'return_distance':False}):
    # Belirli bir kalori miktarına göre öneri yapma fonksiyonu
    extracted_data = extract_data(dataframe, ingredient_filter, max_nutritional_values)
    prep_data, scaler = scaling(extracted_data)
    neigh = nn_predictor(prep_data)
    pipeline = build_pipeline(neigh, scaler, params)
    test_input = np.array([[0] * 9])  # Test verisi oluşturma
    test_input[0, 1] = max_daily_fat  # Maksimum günlük yağ miktarını ayarlama
    recommended_recipe = apply_pipeline(pipeline, test_input, extracted_data)
    return recommended_recipe

recommended_recipe = recommend_by_calories(dataset, 100, max_list)  # Kaloriye göre öneri fonksiyonunu çağırma
# Gereksiz sütunları kaldırma
recommended_recipe.drop(columns=["RecipeId","CookTime","PrepTime","TotalTime"], inplace=True)
recommended_recipe.head(5)  # İlk 5 önerilen tarifi görüntüleme




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