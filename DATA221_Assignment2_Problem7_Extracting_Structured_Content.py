#Mudit Jindal
#Problem7: Extracting Structured Content

import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Data_science"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

print("Title:", soup.title.text)

content = soup.find("div", {"id": "mw-content-text"})
paragraphs = content.find_all("p")

for p in paragraphs:
    text = p.get_text().strip()
    if len(text) >= 50:
        print("\nFirst paragraph:")
        print(text)
        break
