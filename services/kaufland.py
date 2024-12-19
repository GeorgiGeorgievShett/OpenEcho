import requests

def check_kaufland_email(email):
    url = "https://account.kaufland.com/pages-web/api/user-exists"
    params = {
        "client_id": "176c4d02-5a23-4172-a12b-d2412f25a0d4",
        "lang": "en-GB,en-US;q=0.9,en;q=0.8",
        "preferredStore": "BG2200",
        "return_url": "https://www.kaufland.bg/",
        "ui_locales": "bg",
        "view_type": "login",
        "username": email,
        "usernameType": "email",
        "requestId": "fe2a66cc-cd86-4d11-b823-74a53e6fb71d",
        "_data": "routes/$pages/api.user-exists",
    }
 
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "Referer": "https://account.kaufland.com/pages-web/login",
    }
 
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status() 
        data = response.json()
        if data.get("success"):
            if data.get("userExists"):
                return "user_exists"
            else:
                return "user_does_not_exist"
        else:
            return "unknown_error"
    except requests.exceptions.RequestException as e:
        return "request_error"
