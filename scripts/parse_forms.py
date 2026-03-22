from bs4 import BeautifulSoup

with open('scripts/d2io_dump.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

forms = soup.find_all('form')
print(f"Found {len(forms)} forms.")

for idx, form in enumerate(forms):
    action = form.get('action')
    print(f"\n--- Form {idx} (action: {action}) ---")
    inputs = form.find_all(['input', 'select', 'button'])
    for inp in inputs:
        name = inp.get('name')
        type_ = inp.get('type')
        val = inp.get('value')
        print(f"  {inp.name} name='{name}' type='{type_}' value='{val}'")
