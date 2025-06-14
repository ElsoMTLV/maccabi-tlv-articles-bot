import requests
from bs4 import BeautifulSoup

def get_articles():
    url = "https://tags.walla.co.il/מכבי_תל_אביב_בכדורסל"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    items = soup.select("li.tag_item a.tag_link")

    articles = []
    for item in items[:5]:  # Limit to latest 5
        title = item.get_text(strip=True)
        link = item["href"]
        if not link.startswith("http"):
            link = "https://tags.walla.co.il" + link
        articles.append({"title": title, "url": link})
    return articles
