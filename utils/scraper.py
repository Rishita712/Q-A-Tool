import requests
from bs4 import BeautifulSoup

def scrape_url(url):
    try:
        r = requests.get(url, timeout=10)
        soup = BeautifulSoup(r.content, "html.parser")
        return ' '.join([p.get_text() for p in soup.find_all('p')])
    except Exception as e:
        return f"Error fetching URL: {e}"
