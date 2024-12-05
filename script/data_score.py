import pandas as pd

# CSV dosyasını oku
csv_dosya_adi = "./Data/raw_data/recipes.csv"  # Dosya adını belirtin
veriler = pd.read_csv(csv_dosya_adi)

# Toplam satır sayısını yazdır
print(f"CSV dosyasındaki toplam veri sayısı: {len(veriler)}")

#  522517 adet veri var şuan 