import requests

def chitanka_login_check(email):
    try:
        if "@" in email:
            username = email.split("@")[0]
        else:
            username = email
        
        session = requests.Session()
        
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded",
            "Origin": "https://chitanka.info",
            "Referer": "https://chitanka.info/login",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        }
        
        payload = {
            "returnto": "https://chitanka.info/authors/last-name/%D0%9B?cache=1734725385",
            "username": username,
            "password": "321321321",
        }
        
        url = "https://chitanka.info/login"
        response = session.post(url, headers=headers, data=payload)

        if response.status_code == 200:
            if "Не съществува потребител с име" in response.text:
                return "user_does_not_exist"
            elif "Въвели сте грешна парола" in response.text:
                return "user_exists"
        else:
            return "request_error"

    except Exception:
        return "request_error"