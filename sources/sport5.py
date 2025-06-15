import requests
from bs4 import BeautifulSoup

def get_articles():
    url = "https://www.sport5.co.il/team.aspx?FolderID=2592"
    res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "html.parser")
    articles = []

    for item in soup.select(".listItem a")[:10]:  # Limit to recent items
        link = item.get("href")
        title = item.get_text(strip=True)

        if not link or not title:
            continue

        if not link.startswith("http"):
            link = "https://www.sport5.co.il" + link

        articles.append({
            "title": title,
            "url": link
        })

    return articles
