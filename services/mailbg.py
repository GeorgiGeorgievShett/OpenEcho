import aiohttp
from urllib.parse import quote

async def check_username_registration(email_or_username):
    if '@mail.bg' not in email_or_username:
        username = email_or_username.split('@')[0]
        email = f"{username}@mail.bg"
    else:
        email = email_or_username

    encoded_email = quote(email)
    url = f'https://mail.bg/signup/checkuser/format/json/user/{encoded_email}'

    headers = {
        'Accept': 'application/json, text/javascript, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }

    cookies = {
        'OAID': '1234567890abcdef',
        'current_page': 'mailbox/inbox',
        's': 'abcdef1234567890',
        't': 'q7_w9g-42_s.e3r7.28.bg',
        'vid': '0987654321fedcba' 
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, cookies=cookies) as response:
                response.raise_for_status()

                try:
                    response_json = await response.json()
                except ValueError:
                    return "response_not_json"

                if response_json.get('result') is True:
                    return "user_does_not_exist"
                elif response_json.get('result') is False:
                    return "user_exists"
                else:
                    return "unknown_response"
    except aiohttp.ClientError:
        return "request_error"
    except ValueError:
        return "request_error"