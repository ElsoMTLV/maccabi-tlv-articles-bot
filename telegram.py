import requests

def send_article(token, chat_id, article):
    text = f"{article['title']}\n{article['url']}"
    try:
        response = requests.post(
            f"https://api.telegram.org/bot{token}/sendMessage",
            data={"chat_id": chat_id, "text": text}
        )
        response.raise_for_status()
        print(f"✅ Sent: {article['title']}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Failed to send: {article['title']}\n{e}")
