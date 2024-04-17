from bs4 import BeautifulSoup
import requests

URL = 'https://www.scrapethissite.com/pages/simple/'

response = requests.get(URL)

if response.status_code == 200:

    soup = BeautifulSoup(response.text, 'html.parser')
 
    pays = soup.find_all('div', class_='country-name')

    for element in pays:
        print(element.text)
else:
    print ("Erreur lors de la connexion au site")
