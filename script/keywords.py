import pandas as pd

# CSV dosyasını yükleme
data = pd.read_csv('./Data/raw_data/recipes.csv')

# Keywords sütunundaki tüm anahtar kelimeleri temizleme ve benzersiz olanları tutma
keywords = data['Keywords'].dropna().apply(lambda x: x.strip('c()').replace('"', '').split(', '))

# Tüm anahtar kelimeleri bir listeye ekleme
all_keywords = [keyword for sublist in keywords for keyword in sublist]

# Benzersiz anahtar kelimeleri bulma
unique_keywords = set(all_keywords)

# Benzersiz anahtar kelimeleri yazdırma
for keyword in unique_keywords:
    print(keyword)
    
    