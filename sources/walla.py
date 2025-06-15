import requests
from bs4 import BeautifulSoup

def get_articles():
    url = "https://tags.walla.co.il/%D7%9E%D7%9B%D7%91%D7%99_%D7%AA%D7%9C_%D7%90%D7%91%D7%99%D7%91_%D7%91%D7%9B%D7%93%D7%95%D7%A8%D7%A1%D7%9C"
    res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "html.parser")
    articles = []

    for item in soup.select("article a")[:10]:
        link = item.get("href")
        title = item.get_text(strip=True)

        if not link or not title:
            continue

        if not link.startswith("http"):
            link = "https://www.walla.co.il" + link

        articles.append({
            "title": title,
            "url": link
        })

    return articles
