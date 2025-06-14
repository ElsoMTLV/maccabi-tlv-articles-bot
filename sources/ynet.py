import requests
from bs4 import BeautifulSoup

def get_articles():
    url = "https://www.ynet.co.il/topics/מכבי_תל_אביב_בכדורסל"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    items = soup.select("article a")

    articles = []
    for item in items[:5]:
        title = item.get_text(strip=True)
        href = item.get("href")
        if href and "/article/" in href:
            link = "https://www.ynet.co.il" + href
            articles.append({"title": title, "url": link})
    return articles
