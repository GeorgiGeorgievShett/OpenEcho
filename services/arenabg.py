import aiohttp
from bs4 import BeautifulSoup


async def check_username_registration(email):
    async with aiohttp.ClientSession() as session:
        login_url = "https://arenabg.com/bg/users/signin/"
        login_data = {
            "username_or_email": email,
            "password": '321321321'
        }

        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Referer": "https://arenabg.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
        }

        async with session.post(login_url, data=login_data, headers=headers) as response:
            if response.status == 200:
                page_text = await response.text()
                soup = BeautifulSoup(page_text, 'html.parser')
                page_text = soup.get_text()

                if 'грешна' in page_text.lower():
                    return "user_exists"
                elif 'не е намерен' in page_text.lower():
                    return "user_does_not_exist"
                else:
                    return "unknown_response"
            else:
                return "unknown_response"