import aiohttp

async def check_username_registration(email):
    url = 'https://www.plovdiv24.bg/js/nkselect.php'

    params = {
        'switch': 'check',
        'userid': '',
        'obekt': 'regemail',
        'value': email
    }

    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url, params=params) as response:
                response.raise_for_status()

                response_text = await response.text()

                if 'Този e-mail вече е регистриран!' in response_text:
                    return "user_exists"
                elif 'hasemail=1' in response_text:
                    return "user_does_not_exist"
                else:
                    return "unknown_response"

        except aiohttp.ClientError:
            return "request_error"