import cloudscraper
import json
import re

html = cloudscraper.create_scraper().get('https://d2trader.net/api/market/items').text
m = re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>', html)
if m:
    data = json.loads(m.group(1))
    print(list(data.get('props', {}).get('pageProps', {}).keys()))
else:
    print("No NEXT_DATA found!")

if html.startswith('[') or html.startswith('{'):
    print("Wait, it IS JSON!")
else:
    print(html[:500])
