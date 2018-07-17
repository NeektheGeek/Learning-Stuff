import requests
from bs4 import BeautifulSoup

def search_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'https://thenewboston.com/search.php?type=1&sort=pop&page=' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        for link in soup.findAll('a', {'cclass': 'user-name'}):
            href = link.get('href')
            print(href)
        page += 1

search_spider(3)