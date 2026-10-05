import requests
import pandas as pd
from bs4 import BeautifulSoup

reviews_data = []

for page in range(1,21):

    website = f'https://www.empireonline.com/movies/reviews/{page}/'
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/154.0.0.0 Safari/537.36'
    }
    
    r = requests.get(website, headers=headers)
    
    soup = BeautifulSoup(r.content, 'html.parser')
    
    empire = soup.find_all('div',class_='category-module-scss-module__EgQJaa__category content-area')
    
    link_list = []
    for item in empire:
    
        links = item.find_all('a', href=True)
    
        for link in links:
            #print(link['href'])
            if link['href'].startswith('https'):
                link_list.append(link['href'])
        #print('\n'.join(link_list))
        links = list(set(link_list))
        #print(links)
    
        for li in links:
            li_website = f'{li}'
            li_r = requests.get(li_website, headers=headers)
            li_soup = BeautifulSoup(li_r.content, 'html.parser')
    
            
            movie_name_t = None
            review_by_t = None
            rating_t = None
            actors_t = None
            review_summary_t = None
            review_t = None
            about_movie_t = None
            movie_name_try2 = None

            #link feature
            link_t = li

            #movie_name feature
            try:
                movie_name_t = li_soup.find('div', class_='infoGrid-module-scss-module__Dxi0aG__info-grid-item').get_text(strip=True)
            except AttributeError:
                pass

            #movie-name_try2 as if movie_name feature fail
            try:
                movie_name_try2_t = li_soup.find('h1', class_='title-module-scss-module__kn5gma__h1 undefined').get_text(strip=True)
            except AttributeError:
                pass

            #movie about_movie feature
            try:
                about_movie_t = li_soup.find('div',class_='nutshell-module-scss-module__qhW9IG__nutshell nutshell').get_text(strip=True)
            except AttributeError:
                pass

            #movie review feature
            try:
                review_by_t = li_soup.find('a', class_='authorDate-module-scss-module__27DeVq__author__name').get_text(strip=True)
            except AttributeError:
                pass

            # Fetch all review content
            review_content = li_soup.find_all('span', attrs={'data-test': 'content'}) 
        
            review_list = []
            for item in review_content:
                text = item.get_text(" ", strip=True)
                review_list.append(text)
                
            #movie review feature
            review_t = '\n\n'.join(review_list)

            #movie review summary feature
            try:
                review_summary_t = li_soup.find('div', class_ = 'verdict-module-scss-module__d9chWq__verdict').get_text(strip=True)
            except AttributeError:
                pass

            actors_fetching = li_soup.find_all('div', class_='entityLinks-module-scss-module__yOlnna__entity-link')

            #cast feature
            try:
                actors_t = []
                for item in actors_fetching:
                    actor_names = item.find('a').get_text(strip=True)
                    if actor_names not in actors_t:
                        actors_t.append(actor_names)
            except AttributeError:
                pass
    

            #movie ratng feature
            try:
                rating_t = len(li_soup.find_all('span', class_ = 'ratings-module-scss-module__q_BhfG__rating__on'))
            except AttributeError:
                pass
        
            all_features = {
                'link': link_t,
                'movie_name': movie_name_t, 
                'movie_name_try2': movie_name_try2_t, 
                'about_movie': about_movie_t, 
                'review_by': review_by_t, 
                'review': review_t,  
                'review_summary': review_summary_t, 
                'cast': actors_t, 
                'rating_out5': rating_t 
            }


            reviews_data.append(all_features)
    
    
    df = pd.DataFrame(reviews_data)
    df.to_csv('movie_reviews_empire.csv', index=False)
    
        