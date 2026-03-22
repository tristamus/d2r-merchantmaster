import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

url = "https://diablo2.io/price-check/?keywords=Enigma"
req = urllib.request.Request(
    url, 
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
)
try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        
        # In phpBB (diablo2.io is phpBB based), search results usually have a specific class.
        # Let's find all topics or posts.
        results = soup.select('.row')
        for idx, row in enumerate(results[:20]):
            title_tag = row.select_one('.topictitle')
            if title_tag:
                title = title_tag.text.strip()
                # Price data might be in another span.
                print(f"[{idx}] Title: {title}")
                # We can also dump the HTML of the first valid row to see its structure
                if idx == 0:
                    print("--- HTML ---")
                    print(row.prettify())
                    print("------------")
except Exception as e:
    print("Error:", e)
