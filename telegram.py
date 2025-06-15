import requests

def send_article(token, chat_id, article):
    text = f"{article['title']}\n{article['url']}"
    try:
        response = requests.post(
            f"https://api.telegram.org/bot{token}/sendMessage",
            data={"chat_id": chat_id, "text": text}
        )
        print("Sent to Telegram:", article['title'], response.status_code)
        if response.status_code != 200:
            print("Telegram Error:", response.text)
    except Exception as e:
        print("Exception while sending Telegram message:", e)
