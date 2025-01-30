import aiohttp

async def check_username_registration(email: str):
    url = f"https://id.accounts.sportal.bg/native/emails/{email}?brand=sportal"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.64 Safari/537.36',
        'Referrer-Policy': 'same-origin'
    }

    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url, headers=headers) as response:
                response.raise_for_status()

                if response.status == 200:
                    response_json = await response.json()
                    exists_in_native = response_json.get("existsInNative", False)
                    exists_in_legacy = response_json.get("existsInLegacy", False)

                    if not exists_in_native and not exists_in_legacy:
                        return "user_does_not_exist"
                    elif exists_in_native:
                        return "user_exists"
                else:
                    return "unknown_response"

        except aiohttp.ClientError as e:
            return "request_error"
