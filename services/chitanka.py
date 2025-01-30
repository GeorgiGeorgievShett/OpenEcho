import aiohttp


async def check_username_registration(email):
    """
    Asynchronously checks the username registration for Chitanka.info.
    """
    try:
        login_url = "https://chitanka.info/login"

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded",
            "Origin": "https://chitanka.info",
            "Referer": "https://chitanka.info/login",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        }

        payload = {
            "returnto": "https://chitanka.info/authors/last-name/%D0%9B?cache=1734725385",
            "username": email,
            "password": "321321321",
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(login_url, headers=headers, data=payload) as response:
                response.raise_for_status()

                response_text = await response.text()

                if "Не съществува потребител с име" in response_text:
                    return "user_does_not_exist"
                elif "Въвели сте грешна парола" in response_text:
                    return "user_exists"
                else:
                    return "request_error"

    except aiohttp.ClientError:
        return "request_error"