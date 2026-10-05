import requests
import pandas as pd
from bs4 import BeautifulSoup
import re

beyoung_data=[]

website = 'https://www.beyoung.in/mens-shirts'

r = requests.get(website)
soup = BeautifulSoup(r.content, 'html.parser')
products = soup.select('div.grid.grid-flow-dense.grid-cols-3.gap-4 a[href]')

shirts_links = []

for product in products:
    href = product.get('href')
    if not href.startswith('http'):
        href = 'https://www.beyoung.in/' + href
    shirts_links.append(href)


for link in shirts_links:
    r_li = requests.get(link)
    soup_li = BeautifulSoup(r_li.content, 'html.parser')

    prod_name_t = None
    prod_price_t = None
    prod_fabric_t = None
    prod_neck_t = None
    prod_pattern_t = None
    prod_sleeve_t = None 
    prod_fit_t = None
    prod_style_t = None
    prod_rating_t = None

    items_link_t = link
    
    try:
        prod_name_t = soup_li.find('h1').get_text()
    except AttributeError:
        pass

    try:
        prod_price_t = soup_li.find('h2').get_text()
    except AttributeError:
        pass

    try:
        prod_fabric_t = soup_li.find('div', string= lambda x:x and x.strip()=='Fabric').find_next('div').get_text(strip=True)
    except AttributeError:
        pass

    try:
        prod_neck_t = soup_li.find('div', string= lambda x:x and x.strip()=='Neck').find_next('div').get_text(strip=True)
    except AttributeError:
        pass

    try:
        prod_pattern_t = soup_li.find('div', string= lambda x:x and x.strip()=='Pattern').find_next('div').get_text(strip=True)
    except AttributeError:
        pass

    try:
        prod_sleeve_t = soup_li.find('div', string= lambda x:x and x.strip()=='Sleeve').find_next('div').get_text(strip=True)
    except AttributeError:
        pass

    try:
        prod_fit_t = soup_li.find('div', string= lambda x:x and x.strip()=='Fit').find_next('div').get_text(strip=True)
    except AttributeError:
        pass

    try:
        prod_style_t = soup_li.find('div', string= lambda x:x and x.strip()=='Style').find_next('div').get_text(strip=True)
    except AttributeError:
        pass

    try:
        html = r_li.text
        rating_match = re.search(r'avrage_rating\\?":([\d.]+)', html)
        if rating_match:
            prod_rating_t = rating_match.group(1)
    except Exception:
        pass

    all_features = {
        'items_link': items_link_t,
        'prod_name':prod_name_t,
        'prod_price':prod_price_t,
        'prod_fabric':prod_fabric_t,
        'prod_neck':prod_neck_t,
        'prod_pattern':prod_pattern_t,
        'prod_sleeve':prod_sleeve_t,
        'prod_fit':prod_fit_t,
        'prod_style':prod_style_t,
        'prod_rating':prod_rating_t
    }

    beyoung_data.append(all_features)
    
df = pd.DataFrame(beyoung_data)
df.to_csv('beyoung_data.csv', index=False)

    
    