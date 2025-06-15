import requests
from bs4 import BeautifulSoup

def get_articles():
    url = "https://www.sport5.co.il/team.aspx?FolderID=2592"
    res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "html.parser")
    articles = []

    for block in soup.select("div.articleBannerSpace")[:10]:  # recent items
        a_tag = block.find("h2")
        if not a_tag:
            continue

        link_tag = a_tag.find("a")
        if not link_tag:
            continue

        href = link_tag.get("href")
        title = link_tag.get_text(strip=True)

        if not href or not title:
            continue

        # Ensure full URL
        if not href.startswith("http"):
            href = "https://www.sport5.co.il" + href

        articles.append({
            "title": title,
            "url": href
        })

    return articles
