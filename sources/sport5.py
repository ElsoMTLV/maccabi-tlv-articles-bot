import requests
from bs4 import BeautifulSoup

def get_articles():
    url = "https://www.sport5.co.il/team.aspx?FolderID=2592"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    items = soup.select("ul#articleList li a")

    articles = []
    for item in items[:5]:
        title = item.get("title", "").strip()
        link = item["href"]
        if not link.startswith("http"):
            link = "https://www.sport5.co.il" + link
        if title:
            articles.append({"title": title, "url": link})
    return articles
