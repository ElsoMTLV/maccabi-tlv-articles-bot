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
        all_articles.extend(scraper.get_articles())
    except Exception as e:
        print(f"Error with {scraper.__name__}: {e}")

# Filter new articles
new_articles = [a for a in all_articles if a["url"] not in sent_urls]

# Send new articles
for article in new_articles:
    send_article(BOT_TOKEN, CHAT_ID, article)
    sent_urls.add(article["url"])

# Save updated list of sent URLs
with open(SENT_FILE, "w") as f:
    json.dump(list(sent_urls), f)

print(f"✅ Sent {len(new_articles)} new articles")
