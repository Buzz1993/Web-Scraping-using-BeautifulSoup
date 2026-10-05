import requests
import pandas as pd
from bs4 import BeautifulSoup

quote_data = []

for pages in range(1,11):
    website = f"https://quotes.toscrape.com/page/{pages}/"
    
    r = requests.get(website)
    soup = BeautifulSoup(r.content, "html.parser")
    quote = soup.find_all("div", class_ = "quote")
    
    
    for item in quote:
        quote_text = item.find('span').get_text()
        author_name = item.find('small').get_text()
        #print(author_name)
        tags = item.find('meta')['content']
        half_link = item.find('a')['href']
        full_link = (f"https://quotes.toscrape.com/{half_link}")
        inner_website = full_link
        r_inner = requests.get(inner_website)
        soup_inner = BeautifulSoup(r_inner.content, "html.parser")
        inner_author_name = soup_inner.find('h3').get_text()
        if inner_author_name == author_name:
            author_birth_date = soup_inner.find('span').get_text()
            born_place = soup_inner.find('span', class_ = "author-born-location").get_text()
            about_author  = soup_inner.find('div', class_ = 'author-description').get_text()
    
        all_features = {
            "quote": quote_text,
            "author_name": author_name,
            "tags": tags,
            "author_birth_date": author_birth_date,
            "born_place": born_place,
            "about_author": about_author
        }
    
        quote_data.append(all_features)
    
df = pd.DataFrame(quote_data)
df.to_csv("Quote_data.csv", index=False)