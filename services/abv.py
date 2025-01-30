import aiohttp


async def check_username_registration(email):
    """
    Asynchronously checks the username registration for ABV.bg.
    """
    username = email.split('@')[0]
    base_url = 'https://passport.abv.bg/app/profiles/validateename'

    params = {
        'id': username,
        'fname': '',
        'lname': '',
        'byear': ''
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(base_url, params=params) as response:
                response.raise_for_status()
                
                response_text = await response.text()

                if '<result>info.showcaptcha</result>' in response_text:
                    return "captcha_error"
                if '<result>info.occupied</result>' in response_text:
                    return "user_exists"
                elif '<result>info.free</result>' in response_text:
                    return "user_does_not_exist"
                else:
                    return "unknown_error"

    except aiohttp.ClientError:
        return "request_error"