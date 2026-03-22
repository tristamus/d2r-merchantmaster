import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

item_name = urllib.parse.quote('Ber')
url = f"https://diablo2.io/search.php?keywords={item_name}&terms=all&author=&fid%5B%5D=16&sc=0&sf=titleonly&sr=topics&sk=t&sd=d&st=0&ch=300&t=0&activesold=1&submit=Search"

req = urllib.request.Request(
    url, 
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
)
try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        
        with open('scripts/search_results.html', 'w', encoding='utf-8') as f:
            f.write(html)
            
        print("Page title:", soup.title.string if soup.title else "No title")
        print("Size:", len(html))
        
        # PHPBB3 topics are often in ul.topiclist li.row
        topics = soup.select('div.search-results li.row') or soup.select('li.row')
        print(f"URL: {url}")
        print(f"Found {len(topics)} topics")
        
        for idx, topic in enumerate(topics[:10]):
            title_tag = topic.select_one('.topictitle')
            if title_tag:
                print(f"[{idx+1}] {title_tag.text.strip()}")
            else:
                print(f"[{idx+1}] {topic.text[:100].strip()}")
                
except Exception as e:
    print("Error:", e)
