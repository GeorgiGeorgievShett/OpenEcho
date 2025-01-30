import aiohttp
from bs4 import BeautifulSoup

async def check_username_registration(email):
    session = aiohttp.ClientSession()

    try:
        initial_url = "https://www.forlife.bg/my-account"
        async with session.get(initial_url) as response:
            response.raise_for_status()
            soup = BeautifulSoup(await response.text(), 'html.parser')
            nonce_input = soup.find("input", {"name": "woocommerce-login-nonce"})

            if nonce_input and nonce_input.get("value"):
                login_nonce = nonce_input["value"]
            else:
                return "request_error"
    except aiohttp.ClientError:
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
        async with session.post(login_url, headers=headers, data=payload) as response:
            response.raise_for_status()

            if "Паролата, която въведохте за имейл" in await response.text():
                return "user_exists"
            elif "Непознат имейл адрес" in await response.text():
                return "user_does_not_exist"
            else:
                return "request_error"
    except aiohttp.ClientError:
        return "request_error"
    finally:
        await session.close()