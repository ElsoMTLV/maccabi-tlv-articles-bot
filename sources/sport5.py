import requests
from bs4 import BeautifulSoup

def get_articles():
    url = "https://www.sport5.co.il/team.aspx?FolderID=2592"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/114.0.0.0 Safari/537.36",
        "Accept-Language": "he,en-US;q=0.9,en;q=0.8",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    }

    res = requests.get(url, headers=headers, timeout=10)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "html.parser")
    articles = []

    for block in soup.select("div.articleBannerSpace")[:10]:
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

        if not href.startswith("http"):
            href = "https://www.sport5.co.il" + href

        articles.append({
            "title": title,
            "url": href
        })

    return articles
