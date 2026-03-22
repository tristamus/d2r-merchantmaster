import cloudscraper

scraper = cloudscraper.create_scraper()
html = scraper.get("https://diablo2.io/price-check/", timeout=15).text
with open("price_check.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Saved price_check.html")
