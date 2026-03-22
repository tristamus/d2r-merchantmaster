import urllib.request
import urllib.parse
import sys

url = "https://diablo2.io/price-check/?keywords=Enigma"
req = urllib.request.Request(
    url, 
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
)
try:
    with urllib.request.urlopen(req) as response:
        html = response.read()
        with open('scripts/d2io_dump.html', 'wb') as f:
            f.write(html)
        print(f"Saved {len(html)} bytes to d2io_dump.html")
except Exception as e:
    import traceback
    traceback.print_exc()
