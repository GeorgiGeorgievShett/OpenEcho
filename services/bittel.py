import aiohttp


async def check_username_registration(email):
    """
    Asynchronously checks the username registration for Bittel.bg.
    """
    login_url = 'https://www.bittel.bg/account/login'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Origin': 'https://www.bittel.bg',
        'Referer': 'https://www.bittel.bg/account/login',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    payload = {
        'email': email,
        'password': '321321321',
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(login_url, headers=headers, data=payload) as response:
                response.raise_for_status()

                response_text = await response.text()

                if "Не е открит потребител с посочения мейл адрес." in response_text:
                    return "user_does_not_exist"
                elif "Грешна парола. Опитайте отново." in response_text:
                    return "user_exists"
                else:
                    return "request_error"

    except aiohttp.ClientError:
        return "request_error"
