import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


loveandflair = []

website = 'https://loveandflair.com/collections/dresses'

# Open website with Selenium
driver = webdriver.Chrome()
driver.get(website)
time.sleep(3)

#Keep clicking Load More
while True:
    try:
        load_more = driver.find_element(By.CSS_SELECTOR, "button.js-load-more")
        driver.execute_script("arguments[0].click();", load_more)
        #print("Clicked Load More")
        time.sleep(3)
    except:
        #print("No more Load More button")
        break


#Get final page HTML
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')


#Extract product links
product_links = set()
for a in soup.find_all('a', href=True):
    href = a['href']
    if href.startswith('/products/'):
        product_links.add(href)

print(len(product_links))

driver.quit()

f_links = []
for li in product_links:
    f_li = f"https://loveandflair.com/{li}"
    f_links.append(f_li)

for site in f_links:
    r = requests.get(site)
    soup = BeautifulSoup(r.content, 'html.parser')
    print(site)

    product_title_t = None
    product_price_t = None
    product_color_t = None
    product_discription_t = None
    product_size_t = None
    product_composition_t = None
    product_care_t = None
    model_measurements_t = None


    try:
        product_title_t = soup.find('h4', class_='product__title').get_text(strip=True)
        #print(product_title_t)
    except AttributeError:
        pass

    try:
        product_price_t = soup.find('span', class_='money').get_text(strip=True)
        #print(product_price_t)
    except AttributeError:
        pass

    try:
        product_color_t = soup.find('label', class_='color-swatch').get_text(strip=True)
        #print(product_color_t)
    except AttributeError:
        pass

    try:
        product_discription_t = soup.find('div', class_='about__accordion-description').get_text(strip=True)
        #print(product_discription_t)
    except AttributeError:
        pass


    all_features = {
        'site' : site,
        'product_title' : product_title_t,
        'product_price' : product_price_t,
        'product_color' : product_color_t,
        'product_discription' : product_discription_t
    }

    loveandflair.append(all_features)

df = pd.DataFrame(loveandflair)
df.to_csv('loveandflair.csv', index = False)