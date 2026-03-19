import cloudscraper
import json
import re
import sys
import os
import time

BASE_URL = "https://d2trader.net/"

# Targets mapped exactly to the Item Names in index.html FALLBACK_ITEMS
TARGETS = {
    "Jah Rune": "rune/jah-price",
    "Ber Rune": "rune/ber-price",
    "Ist Rune": "rune/ist-price",
    "Lo Rune": "rune/lo-price",
    "Sur Rune": "rune/sur-price",
    "Ohm Rune": "rune/ohm-price",
    "Vex Rune": "rune/vex-price",
    "Enigma": "item/enigma",
    "Grief": "item/grief-phase-blade",
    "Infinity": "item/infinity",
    "Call to Arms": "item/call-to-arms",
    "Heart of the Oak": "item/heart-of-the-oak-flail",
    "Harlequin Crest": "item/harlequin-crest-shako",
    "Arachnid Mesh": "item/arachnid-mesh",
    "The Stone of Jordan": "item/the-stone-of-jordan",
    "Mara's Kaleidoscope": "item/maras-kaleidoscope",
    "Griffon's Eye": "item/griffons-eye"
}

def extract_fg(html):
    m = re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>', html)
    if m:
        try:
            data = json.loads(m.group(1))
            pp = data.get('props', {}).get('pageProps', {})
            fg = pp.get('page', {}).get('item_price', {}).get('fg')
            if not fg:
                fg = pp.get('item_price', {}).get('fg')
            if fg and ('min' in fg or 'low' in fg):
                return {"min": float(fg.get('min', fg.get('low'))), "max": float(fg.get('max', fg.get('high')))}
        except:
            pass
            
    m = re.search(r'>([\d\.]+)\s*-\s*([\d\.]+)\s*(?:FG|Forum Gold)', html, re.IGNORECASE)
    if m:
        return {"min": float(m.group(1)), "max": float(m.group(2))}

    return None

def main():
    print("Starting silent automated price update...")
    scraper = cloudscraper.create_scraper()
    results = {}
    
    for key, path in TARGETS.items():
        try:
            html = scraper.get(BASE_URL + path, timeout=10).text
            fg = extract_fg(html)
            if fg:
                results[key] = fg
            else:
                print(f"Failed to parse layout for {key}. Keeping last known prices. Silent fail.")
                sys.exit(0)
            time.sleep(1) # Prevent aggressive rate limiting
        except Exception as e:
            print(f"Network exception on {key}: {e}. Silent fail.")
            sys.exit(0)
            
    js_content = f"window.D2TRADER_CACHED_PRICES = {json.dumps(results)};"
    output_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "prices.js")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(js_content)
        
    print(f"Successfully updated prices.js with {len(results)} items.")

if __name__ == "__main__":
    main()
