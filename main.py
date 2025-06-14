
from sources import walla, sport5, israelhayom, ynet, one
from telegram import send_article
import json, os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
SEEN_FILE = "sent_articles.json"

try:
    with open(SEEN_FILE, "r") as f:
        sent = set(json.load(f))
except:
    sent = set()

all_articles = []
for scraper in [walla, sport5, israelhayom, ynet, one]:
    all_articles.extend(scraper.get_articles())

new_articles = [a for a in all_articles if a['url'] not in sent]

for article in new_articles:
    send_article(BOT_TOKEN, CHAT_ID, article)
    sent.add(article['url'])

with open(SEEN_FILE, "w") as f:
    json.dump(list(sent), f)
