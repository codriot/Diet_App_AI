import requests
from bs4 import BeautifulSoup

def get_nutrition_links(base_url):
    links = []
    page_number = 1
    while True:
        # Sayfa numarasını URL'ye ekle
        url = f"{base_url}?p={page_number}"
        
        # Web sitesine GET isteği gönder
        response = requests.get(url)

        # Sayfa içeriğini kontrol et
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            
            # Besin öğelerinin href değerlerini içeren tüm a etiketlerini bul
            items = soup.find_all("div", class_="kkAramaSonucItemKutu")
            if not items:
                break  # Eğer veri yoksa döngüyü kır
            
            for item in items:
                a_tag = item.find("a", class_="kkfs16 maviLink d-block")
                if a_tag and 'href' in a_tag.attrs:
                    links.append("https://www.diyetkolik.com" + a_tag['href'])
            
            # Sayfa numarasını artır
            page_number += 1
        else:
            print(f"Sayfaya ulaşılamadı! HTTP Status Code: {response.status_code}")
            break

    return links

# Örnek kullanım
if __name__ == "__main__":
    base_url = "https://www.diyetkolik.com/kac-kalori/kategori/ekmek-ve-tahillar"
    links = get_nutrition_links(base_url)
    for link in links:
        print(link)