import requests 
from bs4 import BeautifulSoup
import pandas as pd

all_books = []

for page in range(1, 4):
    url = f'http://books.toscrape.com/catalogue/page-{page}.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    books = soup.find_all('article', class_='product_pod')
    for book in books:
        all_books.append({
            "Tytuł": book.h3.a['title'],
            "Cena": book.find('p', class_='price_color').text
        })

df = pd.DataFrame(all_books)
df.to_csv('books.csv', index=False)
print('Zapisano do pliku books.csv')
