import os
import json
from telegram import send_article
from sources import walla, sport5, israelhayom, ynet

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# Load previously sent URLs
SENT_FILE = "sent.json"
if os.path.exists(SENT_FILE):
    with open(SENT_FILE, "r") as f:
        sent_urls = set(json.load(f))
else:
    sent_urls = set()

# Scrape all sources
all_articles = []
for scraper in [walla, sport5, israelhayom, ynet]:
    try:
        articles = scraper.get_articles()
        print(f"{scraper.__name__}: {len(articles)} articles found")
        all_articles.extend(articles)
    except Exception as e:
        print(f"Error with {scraper.__name__}: {e}")

# Debug: Show all collected articles
print(f"🔍 Total articles collected: {len(all_articles)}")

# Filter new articles
new_articles = [a for a in all_articles if a["url"] not in sent_urls]

# Debug: Show filtered count
print(f"🆕 New articles to send: {len(new_articles)}")

# Send new articles
for article in new_articles:
    try:
        send_article(BOT_TOKEN, CHAT_ID, article)
        print(f"✅ Sent: {article['title']}")
        sent_urls.add(article["url"])
    except Exception as e:
        print(f"❌ Failed to send: {article['title']}\nError: {e}")

# Save updated list of sent URLs
with open(SENT_FILE, "w") as f:
    json.dump(list(sent_urls), f)

print(f"📤 Done. Sent {len(new_articles)} new articles.")
