import cloudscraper
import urllib.parse
from bs4 import BeautifulSoup
import time

q = urllib.parse.quote("Enigma")
# Removing fid entirely to search all forums
url = f"https://diablo2.io/search.php?keywords={q}&terms=all&author=&sc=0&sf=titleonly&sr=topics&sk=t&sd=d&st=0&ch=300&t=0&activesold=1&submit=Search"

scraper = cloudscraper.create_scraper()
html = scraper.get(url, timeout=15).text
soup = BeautifulSoup(html, 'html.parser')

trades = soup.select('.zf-container-trade')
print(f"Trades found without fid for Enigma: {len(trades)}")

q = urllib.parse.quote("Jah Rune")
url2 = f"https://diablo2.io/search.php?keywords={q}&terms=all&author=&sc=0&sf=titleonly&sr=topics&sk=t&sd=d&st=0&ch=300&t=0&activesold=1&submit=Search"
html2 = scraper.get(url2, timeout=15).text
soup2 = BeautifulSoup(html2, 'html.parser')
trades2 = soup2.select('.zf-container-trade')
print(f"Trades found without fid for Jah Rune: {len(trades2)}")
