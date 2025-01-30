import aiohttp


async def check_username_registration(email, password="generic_password"):
    """
    Asynchronously checks the username registration for Burgas24.bg.
    """
    login_url = 'https://users.burgas24.bg/login.html'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        'Referer': 'http://www.burgas24.bg/',
    }

    payload = {
        'loginemail': email,
        'loginpass': password,
        'urlref': 'http://www.burgas24.bg/',
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(login_url, headers=headers, data=payload) as response:
                response.raise_for_status()

                response_text = await response.text()

                if "Грешна парола!" in response_text:
                    return "user_exists"
                elif "Няма регистрация с посочения email/потребителско име!" in response_text:
                    return "user_does_not_exist"
                else:
                    return "request_error"

    except aiohttp.ClientError:
        return "request_error"