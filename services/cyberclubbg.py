import aiohttp
from bs4 import BeautifulSoup


async def check_username_registration(email):
    """
    Asynchronously checks the username registration for Cyberclub.bg.
    """
    login_page_url = 'https://jobs.cyberclub.bg/Account/Login'
    login_url = 'https://jobs.cyberclub.bg/Account/Login'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Referer': login_page_url,
        'Origin': 'https://jobs.cyberclub.bg',
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(login_page_url, headers=headers) as response:
                response.raise_for_status()

                soup = BeautifulSoup(await response.text(), 'html.parser')
                token_input = soup.find('input', {'name': '__RequestVerificationToken'})
                if not token_input or not token_input.get('value'):
                    return "request_error"

                verification_token = token_input['value']

                payload = {
                    'Email': email,
                    '__RequestVerificationToken': verification_token,
                }

                async with session.post(login_url, headers=headers, data=payload) as response:
                    response.raise_for_status()

                    response_text = await response.text()

                    if '/Account/Register?lang=EN' in response_text:
                        return "user_does_not_exist"
                    elif '/Account/Login?lang=EN' in response_text:
                        return "user_exists"
                    else:
                        return "request_error"

    except aiohttp.ClientError:
        return "request_error"