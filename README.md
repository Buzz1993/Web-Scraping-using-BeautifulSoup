# 🌐 Web Scraping using BeautifulSoup

## 📌 Overview

This project focuses on **web scraping and data extraction using Python**. The goal is to collect useful information from different websites and save it in a structured format for further analysis.

The project covers websites related to **quotes, news, jobs, books, fashion, movies, music, products, and recipes**.

## 📂 Project Structure

```text
├── 1.quotes.toscrape.com/       # Quotes and author information
├── 2.ycombinator.com/           # Hacker News data
├── 3.realpython.github.io/      # Job information
├── 4.books.toscrape.com/        # Book information
├── 5.loveandflair/              # Fashion product data
├── 6.Empire/                    # Movie reviews and ratings
├── 7.Billboard/                 # Music chart data
├── 8.Beyoung/                   # Men's shirt product data
├── 9.allrecipes/                # Recipe information
└── README.md                    # Project documentation
```

## 📊 Data Collected

The project collects different types of information from each website:

- **Quotes:** Quotes, authors, tags, and author details
- **Hacker News:** News titles, points, and users
- **Jobs:** Job title, company, location, and posting date
- **Books:** Book name, price, and link
- **Love & Flair:** Product name, price, color, and description
- **Empire:** Movie name, reviews, ratings, and cast
- **Billboard:** Song, artist, chart position, and weeks on chart
- **Beyoung:** Product name, price, fabric, pattern, fit, and rating
- **Allrecipes:** Recipe name, rating, chef name, ingredients, cooking time, directions, and nutrition

## 🔍 Methodology

### 1. 🌐 Website Access
- Used **Requests** to send HTTP requests and access web pages.
- Used headers where required to access websites.

### 2. 🔎 Data Extraction
- Used **BeautifulSoup** to find and extract required information from HTML.
- Extracted text, links, attributes, and lists from web pages.

### 3. 📄 Pagination & Links
- Scraped data from **multiple pages**.
- Extracted product/article links and visited individual pages for additional details.

### 4. 🛡️ Error Handling
- Used `try-except` to handle missing information.
- Added **retry logic and delays** for websites returning errors such as `403`.

### 5. 💾 Data Storage
- Used **Pandas DataFrame** to organize the scraped data.
- Saved the final data as **CSV files**.

## 🛠️ Technologies Used

- **Python**
- **Requests**
- **BeautifulSoup**
- **Pandas**
- **Regular Expressions (re)**
- **Jupyter Notebook**

## 🚀 Installation

### 1️⃣ Install Required Libraries

```bash
pip install requests beautifulsoup4 pandas
```

### 2️⃣ Import Libraries

```python
import requests
import pandas as pd
from bs4 import BeautifulSoup
```

## 📌 Key Learning Outcomes

- Understanding how **websites are structured using HTML**
- Finding HTML elements using **BeautifulSoup**
- Extracting text, links, and attributes
- Scraping **multiple pages**
- Following links to scrape detailed information
- Handling missing data and HTTP errors
- Using **Pandas to store scraped data**
- Exporting scraped data into **CSV files**

## 🔮 Future Improvements

- Add data cleaning and exploratory data analysis
- Build dashboards using the collected data