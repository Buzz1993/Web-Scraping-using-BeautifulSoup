import requests
import pandas as pd
from bs4 import BeautifulSoup

book_data = []

for page in range(1,51):
    website = f"https://books.toscrape.com/catalogue/page-{page}.html"
    
    r = requests.get(website)
    soup = BeautifulSoup(r.content, 'html.parser')
    book = soup.find_all('li', class_ = 'col-xs-6 col-sm-4 col-md-3 col-lg-3')
    
    for item in book:
        book_name = item.find('a').find('img')['alt'].strip()
        price = item.find('p', class_='price_color').get_text().strip()
        part_book_link = item.find('h3').find('a')['href']
        book_link = f"https://books.toscrape.com/{part_book_link}"
    
        all_features={
            'book_name':book_name,
            'price':price,
            'book_link':book_link
        }
    
        book_data.append(all_features)
    
    
    
    df = pd.DataFrame(book_data)
    df.to_csv('books_data.csv', index=False)