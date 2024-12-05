
## Eğer Backend ile yapay zeka birleşirse olması gereken dosyalama sistemi
diet_app/
├── __init__.py
├── main.py              # Uygulamanın giriş noktası
├── database.py          # Veritabanı bağlantısını ve yapılandırmasını içerir
├── models/
│   ├── __init__.py      # Modelleri içeren birleştirme dosyası
│   └── user.py          # Kullanıcı modelini içerir
│   └── diet.py          # Diyet modelini içerir
├── schemas/
│   ├── __init__.py      # Şemaları birleştiren dosya
│   └── user.py          # Kullanıcı API'si için şemaları içerir
│   └── diet.py          # Diyet API'si için şemaları içerir
├── routers/
│   ├── __init__.py      # Router dosyalarını birleştiren dosya
│   └── user.py          # Kullanıcı işlemleri için router
│   └── diet.py          # Diyet işlemleri için router
└── utils/
    ├── __init__.py      # Yardımcı fonksiyonları birleştiren dosya
    └── enums.py         # Enum tanımlarını içerir (UserType, DietType gibi)
    └── helpers.py       # Yardımcı fonksiyonları içerir

## Eğer sadece yapay zeka kodlayacaksak olması gereken dosyalama sistemi 

diet_app/
│
├── data/
│   ├── raw_data/               # Ham veri dosyaları
│   ├── processed_data/          # İşlenmiş veri dosyaları
│
├── models/
│   ├── trained_model.pkl       # Eğitilmiş modellerin kaydedildiği dosyalar
│   ├── model_training.py       # Model eğitme dosyası
│
├── src/
│   ├── __init__.py             # src modülü tanımlama
│   ├── data_processing.py      # Veri temizleme ve ön işleme
│   ├── feature_engineering.py  # Özellik mühendisliği işlemleri
│   ├── prediction.py           # Tahmin ve analiz
│
├── app.py                      # Ana uygulama dosyası
├── requirements.txt            # Gerekli kütüphaneler
├── README.md                   # Proje açıklaması
└── tests/
    ├── test_data_processing.py # Veri işleme testleri
    ├── test_prediction.py      # Tahmin testleri
