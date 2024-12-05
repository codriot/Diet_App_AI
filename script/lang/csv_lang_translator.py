import pandas as pd
from googletrans import Translator

# CSV dosyasını yükleme
data = pd.read_csv('Data/raw_data/recipes.csv')

# Çevirici oluşturma
translator = Translator()

# Tüm metinleri Türkçeye çevirme fonksiyonu
def translate_text(text):
    try:
        translated = translator.translate(text, src='en', dest='tr')
        return translated.text
    except Exception as e:
        print(f"Error translating text: {text}")
        return text

# Tüm hücreleri çevirme
for column in data.columns:
    data[column] = data[column].astype(str).apply(translate_text)

# Çevrilen verileri yeni bir CSV dosyasına kaydetme
data.to_csv('translated_recipes.csv', index=False)