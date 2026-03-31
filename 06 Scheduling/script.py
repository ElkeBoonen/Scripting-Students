from bs4 import BeautifulSoup
import requests
import json
import time

start = time.time()

url = "***"
response = requests.get(url)

with open("news.json","r") as file:
    news = json.load(file)

titles = [n["titel"] for n in news]

soup = BeautifulSoup(response.content, "xml")
items = soup.find_all("item")
count = 0
for item in items:

    if item.title.text not in titles:
        count += 1
        news.append(
            {
                "titel": item.title.text,
                "artikel":item.description.text,
                "datum":item.pubDate.text
            }
        )

with open("news.json","w") as file:
    json.dump(news, file)

print(count, "artikels toegevoegd")
end = time.time()

print(end-start,"zoveel seconden geduurd")