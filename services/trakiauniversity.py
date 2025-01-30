import aiohttp

async def check_ftt_username_registration(email):
    login_url = 'https://ftt.uni-sz.bg/international-students/login.php'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Origin': 'https://ftt.uni-sz.bg',
        'Referer': 'https://ftt.uni-sz.bg/international-students/login.php',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    payload = {
        'username': email,
        'password': '321321321',
    }

    async with aiohttp.ClientSession() as session:
        try:
            async with session.post(login_url, headers=headers, data=payload) as response:
                response.raise_for_status()

                response_text = await response.text()

                if "No account found with this username" in response_text:
                    return "user_does_not_exist"
                elif "Wrong password" in response_text or "wrong password" in response_text:
                    return "user_exists"
                else:
                    return "request_error"

        except aiohttp.ClientError:
            return "request_error"
