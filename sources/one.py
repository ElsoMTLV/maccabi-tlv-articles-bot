import httpx
from bs4 import BeautifulSoup

def get_articles():
    url = "https://www.one.co.il/Search/?searchtext=%D7%9E%D7%9B%D7%91%D7%99%20%D7%AA%D7%9C%20%D7%90%D7%91%D7%99%D7%91%20%D7%9B%D7%93%D7%95%D7%A8%D7%A1%D7%9C"
    headers = {"User-Agent": "Mozilla/5.0"}

    articles = []

    try:
        with httpx.Client(http2=True, verify=True, timeout=10) as client:
            res = client.get(url, headers=headers)
            res.raise_for_status()

            soup = BeautifulSoup(res.text, "html.parser")

            for item in soup.select(".searchPageContainer .artText")[:10]:
                link_tag = item.find("a")
                if not link_tag:
                    continue

                link = link_tag.get("href")
                title = link_tag.get_text(strip=True)

                if not link.startswith("http"):
                    link = "https://www.one.co.il" + link

                articles.append({
                    "title": title,
                    "url": link
                })

    except Exception as e:
        print(f"Error with sources.one: {e}")

    return articles
