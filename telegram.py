
import requests

def send_article(token, chat_id, article):
    text = f"{article['title']}\n{article['url']}"
    requests.post(f"https://api.telegram.org/bot{token}/sendMessage",
                  data={"chat_id": chat_id, "text": text})
