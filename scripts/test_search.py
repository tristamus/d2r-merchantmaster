import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

url = "https://diablo2.io/search.php?keywords=Enigma"
req = urllib.request.Request(
    url, 
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
)
try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        
        print("Page title:", soup.title.string if soup.title else "No Title")
        results = soup.select('.postbody') or soup.find_all('div', class_=lambda c: c and 'post' in c)
        print(f"Found {len(results)} search results")
        if results:
            print(results[0].text[:500].strip())
except Exception as e:
    print("Error:", e)
