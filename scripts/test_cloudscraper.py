import cloudscraper
import urllib.parse
from bs4 import BeautifulSoup

q = urllib.parse.quote("Enigma")
url = f"https://diablo2.io/search.php?keywords={q}&terms=all&author=&fid%5B%5D=16&sc=0&sf=titleonly&sr=topics&sk=t&sd=d&st=0&ch=300&t=0&activesold=1&submit=Search"

scraper = cloudscraper.create_scraper()
html = scraper.get(url, timeout=15).text

soup = BeautifulSoup(html, 'html.parser')
trades = soup.select('.zf-container-trade')
print(f"Title: {soup.title.string if soup.title else 'No Title'}")
print(f"Contains cf-browser: {'cf-browser-verification' in html}")
print(f"Found {len(trades)} trades")
