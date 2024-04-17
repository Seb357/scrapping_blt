import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "https://www.scrapethissite.com/pages/forms/?page_num={}"

# Initialisation d'une liste pour stocker les données de toutes les pages
data = []

# Parcourir les dix premières pages
for page in range(1, 11):
    response = requests.get(base_url.format(page))
    soup = BeautifulSoup(response.text, 'html.parser')

    # Trouver toutes les lignes de données dans le tableau
    rows = soup.find_all('tr', class_='team')

    for row in rows:
        # Extraire les données de chaque colonne
        name = row.find('td', class_='name').text.strip()
        wins = row.find('td', class_='wins').text.strip()
        losses = row.find('td', class_='losses').text.strip()
        ot_losses = row.find('td', class_='ot-losses').text.strip()
        goals_for = row.find('td', class_='gf').text.strip()
        goals_against = row.find('td', class_='ga').text.strip()

        # Convertir en entier si la chaîne n'est pas vide, sinon utiliser 0 ou une autre valeur par défaut
        wins = int(wins) if wins else 0
        losses = int(losses) if losses else 0
        ot_losses = int(ot_losses) if ot_losses else 0
        goals_for = int(goals_for) if goals_for else 0
        goals_against = int(goals_against) if goals_against else 0
        diff = goals_for - goals_against

        # Ajouter les données à la liste si elles répondent aux critères
        if diff > 0 and goals_against < 300:
            data.append([name, wins, losses, ot_losses, goals_for, goals_against, diff])

# Créer un DataFrame avec les données collectées
df = pd.DataFrame(data, columns=['Name', 'Wins', 'Losses', 'OT Losses', 'Goals For', 'Goals Against', 'Goal Difference'])

# Sauvegarder les données dans un fichier CSV
df.to_csv('result.csv', index=False)
