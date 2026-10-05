import requests
import pandas as pd
from bs4 import BeautifulSoup

billboard_music=[]

website = 'https://www.billboard.com/charts/india-songs-hotw/'

r = requests.get(website)
soup = BeautifulSoup(r.content, 'html.parser')
music = soup.find_all('div', class_ = 'o-chart-results-list-row-container')

for item in music:

    song_name_t = None
    artist_name_t = None
    last_week_trending_t = None
    highest_position_reached_t = None
    weeks_appeard_t = None
    weeks_number1_t = None

    #song_name
    try:
        song_name_t = item.find('h3', id = 'title-of-a-story').get_text(strip = True)
    except AttributeError:
        pass

    #artist_name
    try:
        artist_name_t = item.find('span', class_=lambda x: x and 'a-no-trucate' in x).get_text(strip=True)
    except AttributeError:
        pass

    #last_week_trending rank for song
    try:
        last_week_trending_t = item.find('span', string=lambda x: x and x.strip() == 'LW').find_next('span').get_text(strip=True)
    except AttributeError:
        pass

    #highest position achieved by song 
    try:
        highest_position_reached_t = item.find('span', string = lambda x:x and x.strip() == 'PEAK').find_next('span').get_text(strip=True)
    except AttributeError:
        pass

    #no of weeks song is there on the chart
    try:
        weeks_appeard_t = item.find('span', string = lambda x:x and x.strip() == 'WEEKS ON CHART').find_next('span').get_text(strip = True)
    except AttributeError:
        pass

    #no of weeks song is at number 1
    try:
        weeks_number1_t = item.find('span', string = lambda x:x and x.strip() == 'WEEKS AT NO. 1').find_next('span').get_text(strip = True)
    except AttributeError:
        pass

    all_features = {
        'song_name': song_name_t,
        'artist_name': artist_name_t,
        'last_week_trending': last_week_trending_t,
        'highest_position_reached': highest_position_reached_t,
        'weeks_appeard': weeks_appeard_t,
        'weeks_number1': weeks_number1_t
    }

    billboard_music.append(all_features)

df = pd.DataFrame(billboard_music)
df.to_csv('billboard_music.csv', index=False)