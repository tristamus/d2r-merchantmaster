import cloudscraper
import json
import re
import os

BASE_URL = "https://d2trader.net/"

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')

def main():
    print("Fetching /items API to generate catalog.js...")
    scraper = cloudscraper.create_scraper()
    
    resp = scraper.get(BASE_URL + "items")
    try:
        items = resp.json()
    except Exception as e:
        print("Failed to parse JSON directly:", e)
        return

    simplified = []
    for i in items:
        # Keep it minimal to save space: n = name, p = path, c = category
        name = i.get('item_name')
        cat = i.get('item_quality')
        syn = i.get('item_synonyms', '')
        
        # approximate path for when/if live proxy comes back, or for links
        if cat == 'rune':
            path = f"rune/{slugify(name)}-price"
        else:
            path = f"item/{slugify(name)}"
            
        entry = {"n": name, "p": path, "c": cat}
        
        if syn and syn.lower() != name.lower():
            # item_synonyms is often a comma separated string
            entry["a"] = [s.strip() for s in syn.split(',')]
            
        simplified.append(entry)

    js_content = f"window.D2TRADER_FULL_CATALOG = {json.dumps(simplified)};"
    output_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "catalog.js")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(js_content)
        
    print(f"Successfully created catalog.js with {len(simplified)} items.")

if __name__ == "__main__":
    main()
