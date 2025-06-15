import requests
from bs4 import BeautifulSoup

def get_articles():
    url = "https://www.israelhayom.co.il/tag/מכבי-תל-אביב-בכדורסל"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/114.0.0.0 Safari/537.36",
        "Accept-Language": "he,en-US;q=0.9,en;q=0.8",
    }

    res = requests.get(url, headers=headers, timeout=10)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "html.parser")
    articles = []

    for article in soup.select("article.post")[:10]:
        link_tag = article.select_one("h3.post-title a")
        if not link_tag:
            continue

        href = link_tag.get("href")
        title = link_tag.get_text(strip=True)

        if not href or not title:
            continue

        # Ensure full URL
        if not href.startswith("http"):
            href = "https://www.israelhayom.co.il" + href

        articles.append({
            "title": title,
            "url": href
        })

    return articles
