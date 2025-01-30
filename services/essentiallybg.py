import aiohttp
from bs4 import BeautifulSoup

async def check_username_registration(email):
    login_url = 'https://essentially.bg/moyat-profil/?action=login'
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://essentially.bg',
        'Referer': 'https://essentially.bg/moyat-profil/?action=login',
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(login_url, headers=headers) as response:
                response.raise_for_status()
                soup = BeautifulSoup(await response.text(), 'html.parser')
                nonce_field = soup.find("input", {"name": "woocommerce-login-nonce"})

                if not nonce_field:
                    return "request_error"

                nonce = nonce_field.get("value")

                payload = {
                    'action': 'login',
                    'username': email,
                    'password': 'dummy_password',
                    'woocommerce-login-nonce': nonce,
                    '_wp_http_referer': '/moyat-profil/?action=login',
                    'login': 'Вход',
                }

                async with session.post(login_url, headers=headers, data=payload) as response:
                    response.raise_for_status()

                    if "Непознат имейл адрес." in await response.text():
                        return "user_does_not_exist"
                    elif "Паролата, която въведохте за имейл адреса" in await response.text():
                        return "user_exists"
                    else:
                        return "request_error"

    except aiohttp.ClientError:
        return "request_error"