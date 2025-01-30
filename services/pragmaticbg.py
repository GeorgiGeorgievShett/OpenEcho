import aiohttp

async def check_username_registration(email: str):
    login_url = 'https://pragmatic.bg/wp-login.php'
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://pragmatic.bg',
        'Referer': 'https://pragmatic.bg/wp-login.php',
    }

    payload = {
        'log': email,
        'pwd': 'dummy_password',
        'wp-submit': 'Log In',
        'redirect_to': 'https://pragmatic.bg/wp-admin/',
        'testcookie': '1'
    }

    async with aiohttp.ClientSession() as session:
        try:
            await session.get(login_url, headers=headers)

            async with session.post(login_url, headers=headers, data=payload) as response:
                response.raise_for_status()
                response_text = await response.text()

                if "Unknown email address." in response_text:
                    return "user_does_not_exist"
                elif "Error: The password you entered for the username" in response_text or "Error: The password you entered for the email address" in response_text:
                    return "user_exists"
                else:
                    return "request_error"

        except aiohttp.ClientError as e:
            return "request_error"