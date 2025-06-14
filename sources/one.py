import requests
from bs4 import BeautifulSoup

def get_articles():
    url = "https://www.one.co.il/Search/?searchtext=מכבי תל אביב כדורסל"
    res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(res.text, "html.parser")
    items = soup.select("div.MainTitle a")

    articles = []
    for item in items[:5]:
        title = item.get_text(strip=True)
        link = item["href"]
        if not link.startswith("http"):
            link = "https://www.one.co.il" + link
        articles.append({"title": title, "url": link})
    return articles
