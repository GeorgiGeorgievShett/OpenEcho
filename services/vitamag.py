import aiohttp
from bs4 import BeautifulSoup

async def check_username_registration(email):
    login_url = 'https://vitamag.bg/moyat-profil/'

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

    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(login_url, headers=headers) as response:
                if response.status != 200:
                    return "request_error"

                soup = BeautifulSoup(await response.text(), 'html.parser')
                nonce_input = soup.find('input', {'name': 'woocommerce-login-nonce'})
                if nonce_input and 'value' in nonce_input.attrs:
                    nonce = nonce_input['value']
                else:
                    return "request_error"

                payload = {
                    'username': email,
                    'password': "321321321",
                    'woocommerce-login-nonce': nonce, 
                    '_wp_http_referer': '/moyat-profil/',
                    'login': 'Вход',
                }

                async with session.post(login_url, headers=headers, data=payload) as response:
                    response_text = await response.text()

                    if "Непознат имейл адрес" in response_text:
                        return "user_does_not_exist"
                    elif "Паролата, която въведохте за имейл адреса" in response_text:
                        return "user_exists"
                    else:
                        return "request_error"
        
        except aiohttp.ClientError:
            return "request_error"