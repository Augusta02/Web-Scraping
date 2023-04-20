import requests
from bs4 import BeautifulSoup
from csv import writer
import re

url = 'https://www.newegg.com/PS5-Systems/SubCategory/ID-3762?cm_sp=Cat_PlayStation_1-_-VisNav-_-PS5-Systems'

response= requests.get(url)

content = response.content
# print(content)
soup = BeautifulSoup(content, 'html.parser')

# print(soup.body)
sections = soup.find_all('div', class_= 'item-cell')

with open('./products.csv', 'w', encoding='utf8', newline='') as f:
    thewriter= writer(f)
    header= ['Product_Name', 'Price', 'Shipping Type', 'Discount']
    thewriter.writerow(header)
    for section in sections:
        product_name = section.find('a', class_='item-title').get_text()
        product_ship_type = section.find('li', class_= 'price-ship').get_text()
        discount = section.find('span', class_='price-save-percent')
        discount = 'NaN' if discount == None else discount.get_text()
        product_price = section.find('li', class_='price-current').get_text()
        match = re.search(r"\$[\d,]+(\.\d+)?", product_price).group() 
        info= [product_name, match, product_ship_type, discount]
        thewriter.writerow(info)
    
    
