import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

item_name = urllib.parse.quote('Ber')
url = f"https://diablo2.io/search.php?keywords={item_name}&terms=all&author=&fid%5B%5D=16&sc=0&sf=titleonly&sr=topics&sk=t&sd=d&st=0&ch=300&t=0&activesold=1&submit=Search"

req = urllib.request.Request(
    url, 
    headers={'User-Agent': 'Mozilla/5.0'}
)
try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        
        trades = soup.select('.zf-container-trade')
        print(f"Found {len(trades)} trades.")
        if trades:
            print("--- HTML structure of first trade ---")
            print(trades[0].prettify())
except Exception as e:
    print("Error:", e)
