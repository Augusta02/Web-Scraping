
import pandas as pd 
from bs4 import BeautifulSoup
import requests
import re


listings= []


for i in range(1, 5):
    url = f'https://nigeriapropertycentre.com/for-rent/houses/showtype?page={i}'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.content, "html.parser")
    cards = soup.find_all('div', class_='row property-list')




    for card in cards:
        description= card.find('h4', class_='content-title').get_text()
        type_ = card.find('h3', itemprop='name').get_text()
        location = card.find('address', class_='voffset-bottom-10').get_text()
        price= card.find_all('span', class_='price')[1].get_text()
            
        listings.append([description, type_, location, price])


df = pd.DataFrame
df.to_csv('dca_house_webscraping.csv', index=False)(listings, columns=['Description', 'Type', 'Location', 'Price'])
