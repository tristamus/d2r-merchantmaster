import urllib.request
import urllib.parse
import sys

target = 'https://diablo2.io/price-check/?keywords=Enigma'
url = 'https://api.allorigins.win/raw?url=' + urllib.parse.quote(target)

req = urllib.request.Request(
    url, 
    headers={'User-Agent': 'Mozilla/5.0'}
)
try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        print(f"Loaded {len(html)} bytes from allorigins")
        if "Enigma" in html:
            print("Found Enigma in response")
        if "cf-browser-verification" in html or "Cloudflare" in html:
            print("Cloudflare blocked allorigins")
except Exception as e:
    print("Error:", e)
