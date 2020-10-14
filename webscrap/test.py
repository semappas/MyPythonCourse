import requests, time, csv
from bs4 import BeautifulSoup
 
def get_total_pages():
    r = requests.get("https://www.rithmschool.com/blog")
    soup = BeautifulSoup(r.text, "html.parser")
    last_page_elem = soup.select(".last [href]")
    total_pages = int(last_page_elem[0]["href"][-1])
    return total_pages
 
def get_page_urls():
    base_url = "https://www.rithmschool.com/blog?page="
    urls = [base_url+str(n) for n in range(1,get_total_pages()+1)]
    return urls 
 
with open("scrape_blog_all_pages_functions.csv", "a") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["title", "url", "date"])
 
    for page in get_page_urls():
        r = requests.get(page)
        soup = BeautifulSoup(r.text, "html.parser")
        articles = soup.find_all("article")
 
        for article in articles:
            title = article.find("a").get_text()
            url = article.find("a")["href"]
            date = article.find("time")["datetime"]
            csv_writer.writerow([title, url, date])
        
        time.sleep(5)
        print(f"Completed page: {page}. Waiting 5 seconds")