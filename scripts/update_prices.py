import cloudscraper
import os
import json
import re
import urllib.parse
import time
from bs4 import BeautifulSoup

RUNE_WEIGHTS = {
    'jah': 55, 'ber': 50, 'sur': 25, 'lo': 28, 'ohm': 22, 'vex': 12, 'cham': 10, 'zod': 20, 'ist': 8, 'mal': 4, 'um': 2, 'pul': 1
}

TARGETS = {
    "Jah Rune": "Jah*",
    "Ber Rune": "Ber*",
    "Ist Rune": "Ist*",
    "Lo Rune": "Lo*",
    "Sur Rune": "Sur*",
    "Ohm Rune": "Ohm*",
    "Vex Rune": "Vex*",
    "Enigma": "Enigma",
    "Grief": "Grief",
    "Infinity": "Infinity",
    "Call to Arms": "Call to arms",
    "Heart of the Oak": "Heart of the oak",
    "Harlequin Crest": "Harlequin crest",
    "Arachnid Mesh": "Arachnid mesh",
    "The Stone of Jordan": "Stone of jordan",
    "Mara's Kaleidoscope": "Maras kaleidoscope",
    "Griffon's Eye": "Griffons eye"
}

def estimate_fg(price_str):
    s = price_str.lower().strip()
    m = re.search(r'([\d\.]+)\s*(?:fg|forum gold)', s)
    if m: return float(m.group(1))
    total = 0
    runes_found = re.findall(r'(\d+)?\s*(jah|ber|sur|lo|ohm|vex|cham|zod|ist|mal|um|pul)', s)
    for qty_str, r in runes_found:
        qty = float(qty_str) if qty_str else 1.0
        total += qty * RUNE_WEIGHTS.get(r, 0)
    return total if total > 0 else None

def get_recent_trades(scraper, query):
    q = urllib.parse.quote(query)
    url = f"https://diablo2.io/search.php?keywords={q}&terms=all&author=&fid%5B%5D=16&sc=0&sf=titleonly&sr=topics&sk=t&sd=d&st=0&ch=300&t=0&activesold=1&submit=Search"
    html = scraper.get(url, timeout=15).text
    soup = BeautifulSoup(html, 'html.parser')
    
    if "cf-browser-verification" in html:
        raise Exception("Cloudflare blocked the request.")
        
    trades = soup.select('.zf-container-trade')
    recent = []
    for trade in trades[:10]:
        text = " ".join([t.strip() for t in trade.text.split('\n') if t.strip()])
        m = re.search(r'for\s+(.*?)(?:\s+\d+\s+\d+|$)', text)
        if m:
            price_str = m.group(1).strip()
            price_str = re.sub(r'\s+[a-zA-Z0-9_-]+\s+\d+\s+(?:day|days|hour|hours|min|mins|sec|secs)\s+ago.*', '', price_str).strip()
            price_str = re.sub(r'\s+\d+$', '', price_str).strip()
            recent.append(price_str)
            
    return recent

def main():
    print("Starting diablo2.io price update...")
    scraper = cloudscraper.create_scraper()
    results = {}
    
    for key, search_term in TARGETS.items():
        try:
            print(f"Scraping {search_term}...", end=" ", flush=True)
            trades = get_recent_trades(scraper, search_term)
            print(f"[{len(trades)} trades]")
            
            fg_values = []
            for t in trades:
                fg = estimate_fg(t)
                if fg: fg_values.append(fg)
                
            min_fg = min(fg_values) if fg_values else 0
            max_fg = max(fg_values) if fg_values else 0
            
            if trades:
                results[key] = {"min": min_fg, "max": max_fg, "recent": trades}
                
            time.sleep(8)
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(12)
            
    js_content = f"window.D2TRADER_CACHED_PRICES = {json.dumps(results)};"
    output_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "prices.js")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(js_content)
        
    print(f"Successfully updated prices.js with {len(results)} items from diablo2.io.")

if __name__ == "__main__":
    main()
