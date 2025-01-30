import aiohttp
from bs4 import BeautifulSoup

async def check_username_registration(email):
    """
    Check if an email is already registered on Mediapool.bg by submitting a registration attempt.
    This version includes extraction of the CSRF _nonce token before submitting the form.
    """
    registration_url = 'https://www.mediapool.bg/users/reg' 

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        'Referer': 'https://www.mediapool.bg/',
    }

    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(registration_url, headers=headers) as response:
                response.raise_for_status()

                html_content = await response.text()
                soup = BeautifulSoup(html_content, 'html.parser')
                nonce_input = soup.find('input', {'name': '_nonce'})

                if nonce_input and 'value' in nonce_input.attrs:
                    nonce_value = nonce_input['value']
                else:
                    return "nonce_not_found"

                payload = {
                    '_nonce': nonce_value, 
                    'username': 'Martina',  
                    'email': email, 
                    'password': 'random_password',  
                    'password1': 'random_password',  
                    'terms_consent': '1', 
                    'newsletter_1': '1',  
                }

                async with session.post(registration_url, data=payload, headers=headers) as registration_response:
                    registration_response.raise_for_status()
                    registration_text = await registration_response.text()

                    if "Имейл адресът, който сте въвели, вече е регистриран в Mediapool.bg" in registration_text:
                        return "user_exists"
                    elif "невалидна заявка" in registration_text or "Грешка" in registration_text:
                        return "request_error"
                    else:
                        return "user_does_not_exist"

        except aiohttp.ClientError:
            return "request_error"