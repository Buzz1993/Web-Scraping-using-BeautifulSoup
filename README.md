# 🌐 Web Scraping using BeautifulSoup

## 📌 Overview

This project focuses on **web scraping and data extraction using Python**. The goal is to collect useful information from different websites and save it in a structured format for further analysis.

The project covers websites related to **quotes, news, jobs, books, fashion, movies, music, products, and recipes**.

---

## 📁 Project Structure

```text
BeautifulSoup WebScraping/
│
├── 1.quotes.toscrape.com/
│   ├── Quote_data.csv
│   └── quote_scraping.ipynb
│
├── 2.ycombinator.com/
│   ├── combinator_data.csv
│   └── jupyter_ycombinator.com.ipynb
│
├── 3.realpython.github.io/
│   ├── job_file.csv
│   └── job_data_jupyter.ipynb
│
├── 4.books.toscrape/
│   ├── books_data.csv
│   └── jupyter_book_data.ipynb
│
├── 5.loveandflair/
│   ├── loveandflair.csv
│   └── jupyter_loveandflair.ipynb
│
├── 6.Empire/
│   ├── movie_reviews_empire.csv
│   └── jupyter_empire.ipynb
│
├── 7.Billboard/
│   ├── billboard_music.csv
│   └── jupyter_billboard.ipynb
│
├── 8.Beyoung/
│   ├── beyoung_data.csv
│   └── jupyter_beyoung.ipynb
│
├── 9.allrecipes/
│   ├── allrecipes.csv
│   └── jupyter_allrecipes.ipynb
│
├── README.md
└── .gitignore
```

---

## 📂 Projects & Approach

### 1. Quotes to Scrape

**Website:** https://quotes.toscrape.com/

**Goal:**  
To scrape quotes along with author information from multiple pages of the website.

**Approach:**

1. Used `Requests` to access the Quotes to Scrape website.
2. Scraped **10 pages** using a loop.
3. Used `BeautifulSoup` to parse the HTML content.
4. Extracted the following information from each quote:
   - Quote text
   - Author name
   - Tags
5. Used the author's profile link to open the **author detail page**.
6. Extracted additional author information:
   - Birth date
   - Birth location
   - Author description
7. Stored all extracted information in a Python list.
8. Converted the list into a Pandas DataFrame.
9. Saved the final data into `Quote_data.csv`.

**Data Collected:**

| Column | Description |
|---|---|
| `quote` | Quote text |
| `author_name` | Name of the author |
| `tags` | Tags associated with the quote |
| `author_birth_date` | Author's birth date |
| `born_place` | Author's birth location |
| `about_author` | Description about the author |

**Output:**  
`Quote_data.csv`

...

### 2. Hacker News (Y Combinator)

**Website:** https://news.ycombinator.com/

**Goal:**  
To scrape news information such as news titles, points, and the users who posted the news.

**Approach:**

1. Used `Requests` to access the Hacker News website.
2. Scraped **27 pages** using a loop.
3. Used `BeautifulSoup` to parse the HTML content.
4. Extracted the following information:
   - News heading
   - News points
   - Username who posted the news
5. Stored all the extracted data in a Python list.
6. Converted the list into a Pandas DataFrame.
7. Saved the final data into `combinator_data.csv`.

**Data Collected:**

| Column | Description |
|---|---|
| `news_heading` | News title |
| `news_points` | Points received by the news |
| `points_by_person` | Username who posted the news |

**Output:**  
`combinator_data.csv`

...

### 3. Real Python - Fake Jobs

**Website:** https://realpython.github.io/fake-jobs/

**Goal:**  
To scrape job information such as job title, company name, location, and posting date.

**Approach:**

1. Used `Requests` to access the website.
2. Used `BeautifulSoup` to parse the HTML content.
3. Found all the job listings from the webpage.
4. Extracted the following information:
   - Job title
   - Company name
   - Location
   - Job posting date
5. Stored all the extracted data in a Python list.
6. Converted the list into a Pandas DataFrame.
7. Saved the final data into `job_file.csv`.

**Data Collected:**

| Column | Description |
|---|---|
| `job_title` | Job title |
| `company_name` | Company name |
| `location` | Job location |
| `job_posting_date` | Date when the job was posted |

**Output:**  
`job_file.csv`

...

### 4. Books to Scrape

**Website:** https://books.toscrape.com/

**Goal:**  
To scrape book information such as book name, price, and book link.

**Approach:**

1. Used `Requests` to access the Books to Scrape website.
2. Scraped the **first page** of the website.
3. Used `BeautifulSoup` to parse the HTML content.
4. Extracted the following information:
   - Book name
   - Price
   - Book link
5. Stored all the extracted data in a Python list.
6. Converted the list into a Pandas DataFrame.
7. Saved the final data into `books_data.csv`.

**Data Collected:**

| Column | Description |
|---|---|
| `book_name` | Name of the book |
| `price` | Price of the book |
| `book_link` | Link to the book |

**Output:**  
`books_data.csv`

...

### 5. Love & Flair

**Website:** https://loveandflair.com/

**Goal:**  
To scrape dress product information from multiple pages of the website.

**Approach:**

1. Used `Requests` to access the Love & Flair website.
2. Scraped **6 pages** from the dresses collection.
3. Collected the product links from each page.
4. Used `BeautifulSoup` to parse the HTML content.
5. Opened each product page and extracted:
   - Product title
   - Product price
   - Product color
   - Product description
6. Stored all the extracted data in a Python list.
7. Converted the list into a Pandas DataFrame.
8. Saved the final data into `loveandflair.csv`.

**Data Collected:**

| Column | Description |
|---|---|
| `site` | Product page link |
| `product_title` | Name of the product |
| `product_price` | Price of the product |
| `product_color` | Color of the product |
| `product_discription` | Product description |

**Output:**  
`loveandflair.csv`

...

### 6. Empire Movie Reviews

**Website:** https://www.empireonline.com/movies/reviews/

**Goal:**  
To scrape movie reviews along with movie details, ratings, and cast information.

**Approach:**

1. Used `Requests` with headers to access the Empire website.
2. Scraped **20 pages** of movie reviews.
3. Collected the movie review links from each page.
4. Used `BeautifulSoup` to parse each movie review page.
5. Extracted the following information:
   - Movie name
   - About the movie
   - Reviewer name
   - Full review
   - Review summary
   - Cast
   - Rating out of 5
6. Used an alternative method to get the movie name if the first method failed.
7. Stored all the extracted data in a Python list.
8. Converted the list into a Pandas DataFrame.
9. Saved the final data into `movie_reviews_empire.csv`.

**Data Collected:**

| Column | Description |
|---|---|
| `link` | Movie review page link |
| `movie_name` | Name of the movie |
| `movie_name_try2` | Alternative movie name |
| `about_movie` | Short information about the movie |
| `review_by` | Name of the reviewer |
| `review` | Full movie review |
| `review_summary` | Review summary or verdict |
| `cast` | Cast members |
| `rating_out5` | Movie rating out of 5 |

**Output:**  
`movie_reviews_empire.csv`

...

### 7. Billboard – India Songs

**Website:** https://www.billboard.com/charts/india-songs-hotw/

**Goal:**  
To scrape song and chart information from the Billboard India Songs chart.

**Approach:**

1. Used `Requests` to access the Billboard India Songs chart.
2. Used `BeautifulSoup` to parse the HTML content.
3. Found all the songs listed on the chart.
4. Extracted the following information:
   - Song name
   - Artist name
   - Last week's rank
   - Highest position reached
   - Weeks on the chart
   - Weeks at number 1
5. Stored all the extracted data in a Python list.
6. Converted the list into a Pandas DataFrame.
7. Saved the final data into `billboard_music.csv`.

**Data Collected:**

| Column | Description |
|---|---|
| `song_name` | Name of the song |
| `artist_name` | Name of the artist |
| `last_week_trending` | Song's rank in the previous week |
| `highest_position_reached` | Highest position reached by the song |
| `weeks_appeard` | Number of weeks the song appeared on the chart |
| `weeks_number1` | Number of weeks the song was at number 1 |

**Output:**  
`billboard_music.csv`

...

### 8. Beyoung – Men's Shirts

**Website:** https://www.beyoung.in/mens-shirts

**Goal:**  
To scrape men's shirt product information such as name, price, fabric, pattern, fit, style, and rating.

**Approach:**

1. Used `Requests` to access the Beyoung men's shirts page.
2. Collected the product links from the webpage.
3. Opened each product page to get detailed information.
4. Used `BeautifulSoup` to parse the HTML content.
5. Extracted the following information:
   - Product name
   - Price
   - Fabric
   - Neck
   - Pattern
   - Sleeve
   - Fit
   - Style
   - Rating
6. Used `Regular Expression (re)` to extract the product rating from the page data.
7. Stored all the extracted data in a Python list.
8. Converted the list into a Pandas DataFrame.
9. Saved the final data into `beyoung_data.csv`.

**Data Collected:**

| Column | Description |
|---|---|
| `items_link` | Product page link |
| `prod_name` | Product name |
| `prod_price` | Product price |
| `prod_fabric` | Fabric of the shirt |
| `prod_neck` | Neck type |
| `prod_pattern` | Pattern of the shirt |
| `prod_sleeve` | Sleeve type |
| `prod_fit` | Fit of the shirt |
| `prod_style` | Style of the shirt |
| `prod_rating` | Product rating |

**Output:**  
`beyoung_data.csv`

...

### 9. Allrecipes – Indian Chicken Recipes

**Website:** https://www.allrecipes.com/recipes/1878/world-cuisine/asian/indian/main-dishes/chicken/

**Goal:**  
To scrape Indian chicken recipes along with recipe details, cooking time, ingredients, directions, and nutrition information.

**Approach:**

1. Used `Requests` with headers to access the Allrecipes website.
2. Collected the recipe links from the Indian chicken recipes page.
3. Used a delay between requests to avoid sending requests too quickly.
4. Added retry logic to handle `403` and other request errors.
5. Used `BeautifulSoup` to parse each recipe page.
6. Extracted the following information:
   - Recipe name
   - Rating
   - Chef name
   - Preparation time
   - Cooking time
   - Stand time
   - Marinate time
   - Total time
   - Additional time
   - Servings
   - Ingredients
   - Directions
   - Nutrition information
7. Stored all the extracted data in a Python list.
8. Converted the list into a Pandas DataFrame.
9. Saved the final data into `allrecipes.csv`.

**Data Collected:**

| Column | Description |
|---|---|
| `link` | Recipe page link |
| `recipe_name` | Name of the recipe |
| `rating_out5` | Recipe rating out of 5 |
| `chef_name` | Name of the chef or recipe contributor |
| `prep_time` | Preparation time |
| `cook_time` | Cooking time |
| `stand_time` | Standing time |
| `marinate_time` | Marinating time |
| `total_time` | Total time required |
| `additional_time` | Additional time |
| `servings` | Number of servings |
| `ingredients_list` | Ingredients required for the recipe |
| `direction` | Steps to prepare the recipe |
| `nutrition_list` | Nutrition information |

**Output:**  
`allrecipes.csv`

...

---

## 🔎 General Methodology

The following common approach was used across the different web scraping projects.

### 1. 🌐 Website Access

- Used **Requests** to send HTTP requests and access web pages.
- Used headers where required to access certain websites.

### 2. 🔍 HTML Parsing

- Used **BeautifulSoup** to parse the HTML content.
- Identified the required HTML tags, classes, IDs, and attributes.
- Extracted text, links, and other required information.

### 3. 📄 Pagination & Links

- Scraped data from **multiple pages** where required.
- Used loops to handle pagination.
- Extracted links from listing pages.
- Visited individual product, author, movie, or recipe pages to collect additional information.

### 4. 🛡️ Error Handling

- Used `try-except` to handle missing information.
- Used `None` when a particular value was not available.
- Added **retry logic and delays** for websites where requests could fail.
- Used request headers where required.

### 5. 📊 Data Organization

- Stored the extracted information in Python lists and dictionaries.
- Converted the collected data into **Pandas DataFrames**.

### 6. 💾 Data Storage

- Saved the final scraped data as **CSV files**.
- Each website has its own output file.

---

## 🛠️ Technologies Used

- **Python**
- **Requests**
- **BeautifulSoup**
- **Pandas**
- **Regular Expressions (`re`)**
- **Jupyter Notebook**

### Libraries Used

```python
import requests
import pandas as pd
from bs4 import BeautifulSoup
import re
```

```markdown
For the Allrecipes project, the following Python modules were also used:

```python
import time
import random
```

---

## 🚀 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Buzz1993/Web-Scraping-using-BeautifulSoup.git
```

### 2️⃣ Move into the Project Folder

```bash
cd Web-Scraping-using-BeautifulSoup
```

### 3️⃣ Install Required Libraries

```bash
pip install requests beautifulsoup4 pandas
```

If you want to work with the Jupyter Notebooks:

```bash
pip install jupyter
```

### 4️⃣ Start Jupyter Notebook

```bash
jupyter notebook
```

```markdown
After starting Jupyter Notebook, open any of the 9 project folders and run the notebook for that particular website.

Each website has its own folder containing its scraping notebook and output CSV file.

---

## 📊 Output

The scraped data from each website is saved as a separate CSV file.

| Project | Output File |
|---|---|
| Quotes to Scrape | `Quote_data.csv` |
| Hacker News | `combinator_data.csv` |
| Real Python Jobs | `job_file.csv` |
| Books to Scrape | `books_data.csv` |
| Love & Flair | `loveandflair.csv` |
| Empire Movie Reviews | `movie_reviews_empire.csv` |
| Billboard India Songs | `billboard_music.csv` |
| Beyoung Men's Shirts | `beyoung_data.csv` |
| Allrecipes | `allrecipes.csv` |

---

## 📌 Key Learning Outcomes

Through this project, I learned how to:

- Understand how **websites are structured using HTML**
- Send requests to websites using **Requests**
- Find HTML elements using **BeautifulSoup**
- Extract text, links, and attributes
- Scrape data from **multiple pages**
- Follow links to scrape detailed information
- Handle missing data using `try-except`
- Handle request errors and retries
- Use headers while accessing websites
- Use **Regular Expressions** to extract specific information
- Use **Pandas** to organize scraped data
- Export scraped data into **CSV files**

---

## 🔮 Future Improvements

- Perform **Exploratory Data Analysis (EDA)** on the collected data
- Build dashboards using the scraped datasets
- Improve error handling for different website responses
