from bs4 import BeautifulSoup
import re

with open('scripts/d2io_dump.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# Diablo2.io "Price Checker" usually uses a specific table or div structure for items.
# Let's find all elements that might contain search results.
print("Title of page:", soup.title.string if soup.title else "No Title")

# Let's search for the keywords "Enigma" in the text
results = soup.find_all(string=re.compile('Enigma|Jah|Ber', re.IGNORECASE))
print(f"Found {len(results)} text nodes matching Enigma/Jah/Ber.")

# Let's see if there is an item row class
rows = soup.select('.itembox') or soup.select('.row') or soup.find_all('div', class_=re.compile('post|item|row'))
print(f"Found {len(rows)} possible rows.")

# Let's check the first few rows for text
for idx, row in enumerate(rows[:5]):
    text = re.sub(r'\s+', ' ', row.text).strip()
    print(f"Row {idx}: {text[:150]}...")
