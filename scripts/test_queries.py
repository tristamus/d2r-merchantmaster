import cloudscraper
import urllib.parse
from bs4 import BeautifulSoup
import time

queries = ["Jah*", "Ber*", "Enigma"]
scraper = cloudscraper.create_scraper()

for q_raw in queries:
    q = urllib.parse.quote(q_raw)
    url = f"https://diablo2.io/search.php?keywords={q}&terms=all&author=&fid%5B%5D=16&sc=0&sf=titleonly&sr=topics&sk=t&sd=d&st=0&ch=300&t=0&activesold=1&submit=Search"

    html = scraper.get(url, timeout=15).text
    soup = BeautifulSoup(html, 'html.parser')
    trades = soup.select('.zf-container-trade')
    
    # Check for search error messages
    error = soup.select_one('.error')
    error_text = error.text.strip() if error else "None"
    
    print(f"Query: {q_raw} | Trades: {len(trades)} | Error: {error_text}")
    print(f"Title: {soup.title.string.strip() if soup.title else 'No Title'}")
    time.sleep(6)
