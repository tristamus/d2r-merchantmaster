import re

texts = [
    "WTS SOLD Ber EU LF: Jah or Zod Sold 14 hours ago by Cero17 to UNQ7 fdde for 1 Jah 59 3 rikkabridde 1 day ago",
    "WTS SOLD Ber EU LF: Jah or Zod Sold 1 day ago by Cero17 to rikkabridde for 1 Ber + 1 Ist 42 0 Cero17 1 day ago",
    "WTS SOLD Ber Runes NA LF: Jah Sold 2 days ago by User2 to User3 for 2 Jah 12 1 User2 2 days ago",
    "WTS SOLD Enigma Mage Plate NA LF: Runes Sold 5 days ago by Test to Foo for 3 Ber 1 Lo 10 5 Test 5 days ago"
]

def parse_price(text):
    # Regex to find "for <PRICE> <views> <replies> <last_user> <time> ago"
    # Actually, the views/replies are numbers. 
    # Notice: "for 1 Jah 59 3 rikkabridde 1 day ago" -> price is "1 Jah"
    # "for 1 Ber + 1 Ist 42 0 Cero17 1 day ago" -> price is "1 Ber + 1 Ist"
    
    m = re.search(r'for\s+(.*?)\s+\d+\s+\d+\s+\S+\s+\d+\s+(?:day|days|hour|hours|min|mins|sec|secs)\s+ago', text)
    if m:
        return m.group(1).strip()
    
    # Fallback simpler regex
    m = re.search(r'for\s+(.*?)(?:\s+\d+\s+\d+|$)', text)
    if m:
        return m.group(1).strip()
    return None

for t in texts:
    print(f"Original: {t}")
    print(f"Price: {parse_price(t)}")
    print("-" * 40)
