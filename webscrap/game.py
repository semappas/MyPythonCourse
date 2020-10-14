import requests
from bs4 import BeautifulSoup
from time import sleep
from random import choice

all_quotes = []
base_url="http://quotes.toscrape.com"
url="/page/1"

while url:
    res = requests.get(f"{base_url}{url}")
    print(f"Now Scraping {base_url}{url}...")
    soup = BeautifulSoup(res.text, "html.parser")
    #print(soup.body)
    quotes = soup.find_all(class_="quote")
    #print (quotes)
    for quote in quotes:
        all_quotes.append({
            "text":quote.find(class_="text").get_text(),
            "author":quote.find(class_="author").get_text(),
            "bio_link":quote.find("a")["href"]
        })
    next_btn = soup.find(class_="next")
    url=next_btn.find("a")["href"] if next_btn else None
    sleep(3)
#print(all_quotes)
quote = choice(all_quotes)
print(quote["text"])