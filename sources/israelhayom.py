import requests
from bs4 import BeautifulSoup

def get_articles():
    url = "https://www.israelhayom.co.il/tag/מכבי-תל-אביב-בכדורסל"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    items = soup.select("div.compactArticle a.compactArticle_link")

    articles = []
    for item in items[:5]:
        title = item.get_text(strip=True)
        link = "https://www.israelhayom.co.il" + item["href"]
        articles.append({"title": title, "url": link})
    return articles
