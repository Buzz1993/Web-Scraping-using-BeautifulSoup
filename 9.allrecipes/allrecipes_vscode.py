import time
import random
import requests
import pandas as pd
from bs4 import BeautifulSoup

allrecipes = []

website = "https://www.allrecipes.com/recipes/1878/world-cuisine/asian/indian/main-dishes/chicken/"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/154.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}

r = requests.get(website, headers=headers)
soup = BeautifulSoup(r.text, "html.parser")
links = soup.select("div.loc.fixedContent a.mntl-card-list-items")


li=[]
for link in links:
    li.append(link.get("href"))
#print(li)

# for f_links in li:
#     r_f = requests.get(f_links, headers=headers)
#     soup_f = BeautifulSoup(r_f.text, "html.parser")

for f_links in li:
    time.sleep(random.uniform(2, 4))
    for attempt in range(3):
        r_f = requests.get(f_links, headers=headers)
        print(f"Attempt {attempt + 1}: {r_f.status_code} - {f_links}")

        if r_f.status_code == 200:
            break
        if r_f.status_code == 403:
            time.sleep(5 * (attempt + 1))
    if r_f.status_code != 200:
        print("Skipping:", f_links)
        continue

    soup_f = BeautifulSoup(r_f.text, "html.parser")

    recipe_name_t = None
    rating_out5_t = None
    chef_name_t = None
    prep_time_t = None
    cook_time_t = None
    stand_time_t = None
    marinate_time_t = None
    total_time_t = None
    additional_time_t = None
    servings_t = None
    ingredients_list_t = None
    direction_t = None
    nutrition_list_t = None

    link = f_links

    #recipe name
    try:
        recipe_name_t = soup_f.find('h1', class_='article-heading text-headline-400').get_text(strip=True)
        #print(recipe_name_t)
    except AttributeError:
        pass

    #dish rating out of 5
    try:
        rating_out5_t = soup_f.find('div', class_='comp mm-recipes-review-bar__rating mntl-text-block text-label-300').get_text(strip=True)
        #print(rating_out5_t)
    except AttributeError:
        pass

    #chef name
    try:
        chef_name_t = soup_f.find('a', class_='mntl-attribution__item-name').get_text(strip=True)
        #print(chef_name_t)
    except AttributeError:
        pass

    #recipe preparation time
    try:
        prep_time_t = soup_f.find('div', string=lambda x: x and x.strip() == 'Prep Time:').find_next('div').get_text(strip=True)
        #print(prep_time_t)    
    except AttributeError:
        pass

    #recipe cooking time
    try:
        cook_time_t = soup_f.find('div', string=lambda x: x and x.strip() == 'Cook Time:').find_next('div').get_text(strip=True)
        #print(cook_time_t)    
    except AttributeError:
        pass

    #food rest time
    try:
        stand_time_t = soup_f.find('div', string=lambda x: x and x.strip() == 'Stand Time:').find_next('div').get_text(strip=True)
        #print(stand_time_t)    
    except AttributeError:
        pass

    #marinate time
    try:
        marinate_time_t = soup_f.find('div', string=lambda x: x and x.strip() == 'Marinate Time:').find_next('div').get_text(strip=True)
        #print(marinate_time_t)    
    except AttributeError:
        pass

    #total cooking time
    try:
        total_time_t = soup_f.find('div', string=lambda x: x and x.strip() == 'Total Time:').find_next('div').get_text(strip=True)
        #print(total_time_t)    
    except AttributeError:
        pass

    #additional cooking time
    try:
        additional_time_t = soup_f.find('div', string=lambda x: x and x.strip() == 'Additional Time:').find_next('div').get_text(strip=True)
        #print(additional_time_t)    
    except AttributeError:
        pass

    #serve to people
    try:
        servings_t = soup_f.find('div', string=lambda x: x and x.strip() == 'Servings:').find_next('div').get_text(strip=True)
        #print(servings_t)    
    except AttributeError:
        pass

    #ingredients list
    try:
        ingredients_list_t=[]
        ing_list = soup_f.find_all('ul', class_='mm-recipes-structured-ingredients__list')
        for item in ing_list:
            for i in item.find_all('li'):
                ing = i.get_text(' ', strip=True)
                ingredients_list_t.append(ing)
        #print(ingredients_list_t)
    except AttributeError:
        pass

    #direction to prepare cook
    try:
        direction_t = []
        dirtn = soup_f.find_all('ol',class_='comp mntl-sc-block mntl-sc-block-startgroup mntl-sc-block-group--OL')
        for item in dirtn:
            for i in item.find_all('li'):
                direction = i.find('p')
                if direction:
                    direction_t.append(direction.get_text(' ', strip=True))
        #print(direction_t)
    except AttributeError:
        pass

    #nutrition get from food
    try:
        nutrition_list_t=[]
        nut_list = soup_f.find_all('tbody', class_='mm-recipes-nutrition-facts-summary__table-body')
        for item in nut_list:
            for i in item.find_all('tr'):
                ing = i.get_text(' ', strip=True)
                nutrition_list_t.append(ing)
        #print(nutrition_list_t)
    except AttributeError:
        pass

    all_features={
        'link' : link,
        'recipe_name' : recipe_name_t,
        'rating_out5' : rating_out5_t,
        'chef_name' : chef_name_t,
        'prep_time' : prep_time_t,
        'cook_time' : cook_time_t,
        'stand_time' : stand_time_t,
        'marinate_time' : marinate_time_t,
        'total_time' : total_time_t,
        'additional_time' : additional_time_t,
        'servings' : servings_t,
        'ingredients_list' : ingredients_list_t,
        'direction' : direction_t,
        'nutrition_list' : nutrition_list_t
    }

    allrecipes.append(all_features)

df = pd.DataFrame(allrecipes)
df.to_csv('allrecipes.csv', index=False)
    