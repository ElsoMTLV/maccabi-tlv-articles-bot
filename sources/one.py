import httpx

def get_articles():
    url = "https://www.one.co.il/Search/?searchtext=מכבי תל אביב כדורסל"
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = httpx.get(url, headers=headers, timeout=10.0)
        response.raise_for_status()
        # parse content here...
        return []
    except Exception as e:
        print("Error with sources.one:", e)
        return []
