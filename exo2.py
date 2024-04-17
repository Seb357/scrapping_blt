import requests
from bs4 import BeautifulSoup
url = "https://www.scrapethissite.com/pages/simple/"
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    countries = soup.find_all(class_='country-name')
    capitals = soup.find_all(class_='country-capital')
    for country, capital in zip(countries, capitals):
        print(country.get_text(strip=True), "-", capital.get_text(strip=True))
else:
    print("La requête a échoué avec le code :", response.status_code)