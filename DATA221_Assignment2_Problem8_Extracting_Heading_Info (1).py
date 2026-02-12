#Mudit Jindal
#Problem8: Extracting Heading Info

import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Data_science"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

content = soup.find("div", {"id": "mw-content-text"})
headings = content.find_all("h2")

with open("headings.txt", "w", encoding="utf-8") as file:
    for h in headings:
        text = h.get_text().replace("[edit]", "").strip()

        if not any(word in text for word in ["References", "External links", "See also", "Notes"]):
            file.write(text + "\n")
