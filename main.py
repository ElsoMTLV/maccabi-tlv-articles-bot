import json
import os
from sources import walla, sport5, israelhayom, ynet
from telegram import send_article

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

SENT_FILE = "sent.json"

def normalize_url(url):
    """Normalize URL by removing query parameters, fragments, etc."""
    from urllib.parse import urlparse, urlunparse
    parsed = urlparse(url)
    return urlunparse((parsed.scheme, parsed.netloc, parsed.path, '', '', ''))

def load_sent_urls():
    if os.path.exists(SENT_FILE):
        with open(SENT_FILE, "r") as f:
            return set(json.load(f))
    return set()

def save_sent_urls(urls):
    with open(SENT_FILE, "w") as f:
        json.dump(sorted(urls), f, ensure_ascii=False, indent=2)

def collect_articles():
    all_articles = {}
    sources = [walla, sport5, israelhayom, ynet]

    for source in sources:
        try:
            articles = source.get_articles()
            print(f"{source.__name__}: {len(articles)} articles found")
            for article in articles:
                norm_url = normalize_url(article["url"])
                all_articles[norm_url] = article  # Last one wins if duplicate
        except Exception as e:
            print(f"❌ Error with {source.__name__}: {e}")

    return all_articles

def main():
    sent_urls = load_sent_urls()
    all_articles = collect_articles()

    new_articles = {
        url: article for url, article in all_articles.items() if url not in sent_urls
    }

    print(f"🔍 Total articles collected: {len(all_articles)}")
    print(f"🆕 New articles to send: {len(new_articles)}")

    for url, article in new_articles.items():
        try:
            send_article(BOT_TOKEN, CHAT_ID, article)
            print(f"✅ Sent: {article['title']}")
            sent_urls.add(url)
        except Exception as e:
            print(f"❌ Failed to send article: {article['title']}\n{e}")

    save_sent_urls(sent_urls)
    print(f"📤 Done. Sent {len(new_articles)} new article(s).")

if __name__ == "__main__":
    main()
