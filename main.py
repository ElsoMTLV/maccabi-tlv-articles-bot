import os
from telegram import send_article
from sources import walla, sport5, israelhayom, ynet, one

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

all_articles = []

for scraper in [walla, sport5, israelhayom, ynet, one]:
    all_articles.extend(scraper.get_articles())

for article in all_articles:
    send_article(BOT_TOKEN, CHAT_ID, article)
