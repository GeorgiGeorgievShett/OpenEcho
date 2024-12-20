import requests

def check_vitamag_email(email):
    url = 'https://vitamag.bg/moyat-profil/'
    
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'Origin': 'https://vitamag.bg',
        'Referer': 'https://vitamag.bg/moyat-profil/',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Dest': 'document',
        'Upgrade-Insecure-Requests': '1',
    }

    payload = {
        'username': email,
        'password': "321321321",
        'woocommerce-login-nonce': 'bcb8109f44',
        '_wp_http_referer': '/moyat-profil/',
        'login': 'Вход',
    }

    response = requests.post(url, headers=headers, data=payload)

    if "Непознат имейл адрес" in response.text:
        return "user_does_not_exist"
    elif "Паролата, която въведохте за имейл адреса" in response.text:
        return "user_exists"
    else:
        return "request_error"