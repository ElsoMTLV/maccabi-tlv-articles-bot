import os
from telegram import send_article
from sources import walla, sport5, israelhayom, ynet, one

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
SENT_FILE = "sent_articles.txt"

# Load previously sent URLs
if os.path.exists(SENT_FILE):
    with open(SENT_FILE, "r", encoding="utf-8") as f:
        sent_urls = set(line.strip() for line in f)
else:
    sent_urls = set()

all_articles = []
for scraper in [walla, sport5, israelhayom, ynet, one]:
    try:
        all_articles.extend(scraper.get_articles())
    except Exception as e:
        print(f"Error with {scraper.__name__}: {e}")

new_sent = 0
for article in all_articles:
    if article['url'] not in sent_urls:
        send_article(BOT_TOKEN, CHAT_ID, article)
        sent_urls.add(article['url'])
        new_sent += 1

# Save updated list
with open(SENT_FILE, "w", encoding="utf-8") as f:
    for url in sent_urls:
        f.write(url + "\n")

print(f"✅ Sent {new_sent} new articles")
