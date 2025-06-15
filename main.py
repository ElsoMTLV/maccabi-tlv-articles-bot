import os
from telegram import send_article
from sources import walla, sport5, israelhayom, ynet, one

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

if not BOT_TOKEN or not CHAT_ID:
    print("Missing BOT_TOKEN or CHAT_ID")
    exit(1)

all_articles = []

for scraper in [walla, sport5, israelhayom, ynet, one]:
    try:
        articles = scraper.get_articles()
        print(f"{scraper.__name__} returned {len(articles)} articles")
        all_articles.extend(articles)
    except Exception as e:
        print(f"Error scraping {scraper.__name__}: {e}")

print(f"Total articles found: {len(all_articles)}")

for article in all_articles:
    print("Sending article:", article['title'])
    send_article(BOT_TOKEN, CHAT_ID, article)
