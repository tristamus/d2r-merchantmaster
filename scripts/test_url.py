import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

url = "https://diablo2.io/price-check/Enigma"
req = urllib.request.Request(
    url, 
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
)
try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        
        print("Page title:", soup.title.string if soup.title else "No Title")
        # Look for trade entries
        trades = soup.select('.trade-wrap') or soup.find_all('div', class_=lambda c: c and 'trade' in c.lower())
        print(f"Found {len(trades)} trade wrappers")
        
        # Another common class in phpBB for list items is row or bg1/bg2
        rows = soup.select('.row.bg1, .row.bg2')
        print(f"Found {len(rows)} standard phpbb rows")
        
except Exception as e:
    import traceback
    traceback.print_exc()
