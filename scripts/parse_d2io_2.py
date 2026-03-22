from bs4 import BeautifulSoup
import re

with open('scripts/d2io_dump.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

items = soup.find_all(string=re.compile('Enigma|Jah|Ber', re.IGNORECASE))
print(f"Found {len(items)} text nodes matching Enigma/Jah/Ber.")

for i, text_node in enumerate(items[:5]):
    print(f"\n--- Node {i} ---")
    print(f"Text: {text_node.strip()}")
    # Let's get the parent that is a div or li or tr
    parent = text_node.find_parent(['div', 'li', 'tr'])
    if parent:
        classes = parent.get('class', [])
        print(f"Parent tag: <{parent.name} class='{' '.join(classes)}'>")
        print(f"Content snippet: {parent.text[:200].strip()}")
    else:
        print("No block parent found.")
