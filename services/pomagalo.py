import aiohttp

async def check_username_registration(email: str) -> str:
    url = 'https://www.pomagalo.com/ajax/index.php?0&_time=1725789785078'
    
    headers = {
        'Accept': 'text/javascript, text/html, application/xml, text/xml, */*',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://www.pomagalo.com',
        'Referer': 'https://www.pomagalo.com/',
        'Sec-CH-UA': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        'Sec-CH-UA-Mobile': '?0',
        'Sec-CH-UA-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    
    payload = {
        '_time': '1725789785078',
        'rpn': 'pluginsSystemLoginClean',
        'rut': 'headerLoginContainer',
        'rpcp': '{"mode":2,"tplFilename":"html/base/dashboard/clean/header/login","name":true}',
        'username': email,
        'password': '1231231',
        '1scrd': '66dd764798597',
        'requestUrl': 'https://www.pomagalo.com/'
    }

    async with aiohttp.ClientSession() as session:
        try:
            async with session.post(url, headers=headers, data=payload, ssl=False) as response:
                response.raise_for_status()
                response_text = await response.text()

                if "Грешно потребителско име или e-mail." in response_text:
                    return 'user_does_not_exist'
                elif "Въвели сте грешна парола" in response_text:
                    return 'user_exists'
                else:
                    return 'unknown_response'

        except aiohttp.ClientError as e:
            return 'request_error'