import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

url = "https://diablo2.io/price-check/"
data = urllib.parse.urlencode({'keywords': 'Enigma', 'ver': '1', 'scl': '1'}).encode('utf-8')

req = urllib.request.Request(
    url, 
    data=data,
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
             'Content-Type': 'application/x-www-form-urlencoded'}
)
try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        
        # In phpBB, errors or info might be in a .error or .success class
        message = soup.select_one('.error')
        if message: print("Message:", message.text)
        
        results = soup.select('.itembox') or soup.select('.post') or soup.find_all('div', class_=lambda c: c and 'trade' in c)
        print(f"Found {len(results)} possible result items")
        if results:
            for i in range(min(3, len(results))):
                print(results[i].text[:200].strip().replace('\n', ' '))
        else:
            print("No visible results. Look for links with 'viewtopic' or 'item'")
            links = soup.find_all('a', href=True)
            enigma_links = [l for l in links if 'enigma' in l['href'].lower() or 'enigma' in l.text.lower()]
            print("Enigma links found:", len(enigma_links))
            for l in enigma_links[:5]:
                print(l.text.strip(), l['href'])
except Exception as e:
    print("Error:", e)
