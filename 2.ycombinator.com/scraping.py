import requests
import pandas as pd
from bs4 import BeautifulSoup

comb_data = []

for page in range(1,28):
    website = f'https://news.ycombinator.com/news?p={page}'
    
    r = requests.get(website)
    soup = BeautifulSoup(r.content, 'html.parser')
    comb = soup.find_all('tr', class_='athing submission')
    
    
    for item in comb:

        news_heading = None
        news_points = None
        points_by_person = None
    
        try:
            news_heading = item.find('span', class_='titleline').get_text()
        except AttributeError:
            pass
    
        try:
            news_points = item.find_next_sibling('tr').find('span', class_='score').get_text()
        except AttributeError:
            pass
    
        try:
            points_by_person = item.find_next_sibling('tr').find('a',class_='hnuser').get_text()
        except AttributeError:
            pass
        
    
        all_features = {
            'news_heading':news_heading,
            'news_points':news_points,
            'points_by_person':points_by_person
        }
    
        comb_data.append(all_features)
    
df = pd.DataFrame(comb_data)
df.to_csv('combinator_data.csv', index=False)