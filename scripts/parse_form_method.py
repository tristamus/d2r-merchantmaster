from bs4 import BeautifulSoup

with open('scripts/d2io_dump.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
form = soup.find('form', id='js-item-search') or soup.find('form')
for f in soup.find_all('form'):
    print(f"Form method: {f.get('method', 'GET')} Action: {f.get('action')}")
