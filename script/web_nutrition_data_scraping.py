import requests
from bs4 import BeautifulSoup
import csv
import os
from web_nutrition_link_scraper import get_nutrition_links

def scrape_nutrition_data(url):
    # URL'nin son kısmını başlık olarak kullan
    title = url.split("/")[-1]

    # Web sitesine GET isteği gönder
    response = requests.get(url)

    # Sayfa içeriğini kontrol et
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Besin değerlerini içeren tabloyu bul
        nutrition_table = soup.find("section", class_="kkMikroDegerlerTasiyici")
        
        if nutrition_table:
            rows = nutrition_table.find_all("tr")
            
            # CSV dosyasına yazmak için verileri topla
            headers = ["name"]
            values = [title]
            for row in rows:
                columns = row.find_all("td")
                label = row.find("th").text.strip()
                if columns:
                    value_100g = columns[0].text.strip()
                    value_portion = columns[1].text.strip()
                    headers.append(f"{label} (100 gr)")
                    headers.append(f"{label} (1 Porsiyon)")
                    values.append(value_100g)
                    values.append(value_portion)
                else:
                    headers.append(f"{label} (100 gr)")
                    headers.append(f"{label} (1 Porsiyon)")
                    values.append("Bu değer yok")
                    values.append("Bu değer yok")
            
            # CSV dosyasına yaz
            file_exists = os.path.isfile('dataset.csv')
            with open('dataset.csv', mode='a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                if not file_exists:
                    writer.writerow(headers)
                writer.writerow(values)
        else:
            print("Besin değerleri bulunamadı.")
    else:
        print(f"Sayfaya ulaşılamadı! HTTP Status Code: {response.status_code}")

# Örnek kullanım
if __name__ == "__main__":
    base_url = "https://www.diyetkolik.com/kac-kalori/kategori/et-tavuk-balik"
    links = get_nutrition_links(base_url)
    for link in links:
        scrape_nutrition_data(link)