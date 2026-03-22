import cloudscraper
import urllib.parse
from bs4 import BeautifulSoup
import time

q = urllib.parse.quote("Jah*")
url = f"https://diablo2.io/search.php?keywords={q}&terms=all&author=&fid%5B%5D=16&sc=0&sf=titleonly&sr=topics&sk=t&sd=d&st=0&ch=300&t=0&activesold=1&submit=Search"

scraper = cloudscraper.create_scraper()
html = scraper.get(url, timeout=15).text
soup = BeautifulSoup(html, 'html.parser')

print("Title:", soup.title.string.strip() if soup.title else 'None')
info = soup.select_one('.content')
print("Content:", info.text.strip() if info else 'None')
