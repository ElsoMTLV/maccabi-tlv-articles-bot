import requests
from bs4 import BeautifulSoup

def get_articles():
    url = "https://www.sport5.co.il/team.aspx?FolderID=2592"
    res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "html.parser")
    articles = []

    # Find article blocks - check divs with news item structure
    for item in soup.select(".newsItem, .sliderItem")[:10]:  # limit for safety
        link_tag = item.find("a")
        title_tag = item.find("h3") or item.find("h2") or item.find("span")

        if not link_tag or not title_tag:
            continue

        href = link_tag.get("href")
        title = title_tag.get_text(strip=True)

        if not href or not title:
            continue

        if not href.startswith("http"):
            href = "https://www.sport5.co.il" + href

        articles.append({
            "title": title,
            "url": href
        })

    return articles
