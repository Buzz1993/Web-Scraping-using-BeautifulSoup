import requests
import pandas as pd
from bs4 import BeautifulSoup

job_data = []

website = "https://realpython.github.io/fake-jobs/"

r = requests.get(website)
soup = BeautifulSoup(r.content , "html.parser")
jobs = soup.find_all('div', class_ = 'column is-half')

for item in jobs:
    job_title = item.find('h2').get_text().strip()
    company_name = item.find('h3').get_text().strip()
    location = item.find('p', class_ = 'location').get_text().strip()
    job_posting_date = item.find('time').get_text()

    all_features={
        'job_title': job_title,
        'company_name':company_name,
        'location':location,
        'job_posting_date':job_posting_date
    }

    job_data.append(all_features)


df = pd.DataFrame(job_data)
df.to_csv('job_file.csv', index=False)