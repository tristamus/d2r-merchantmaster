from bs4 import BeautifulSoup

with open('scripts/search_results.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

trades = soup.select('.zf-container-trade')
print(f"Found {len(trades)} trades.")

for i, trade in enumerate(trades[:10]):
    text = " ".join([t.strip() for t in trade.text.split('\n') if t.strip()])
    print(f"[{i+1}] {text}")
