import aiohttp
from bs4 import BeautifulSoup

LOGIN_PAGE_URL = "https://elmak.bg/my-account-2/"
LOGIN_POST_URL = "https://elmak.bg/my-account-2/"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

async def check_username_registration(email):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(LOGIN_PAGE_URL, headers=HEADERS) as response:
                if response.status != 200:
                    print("Failed to fetch the login page.")
                    return "request_error"

                page_content = await response.text()

            soup = BeautifulSoup(page_content, 'html.parser')
            nonce_input = soup.find("input", {"id": "woocommerce-login-nonce", "name": "woocommerce-login-nonce"})

            if not nonce_input or not nonce_input.has_attr("value"):
                print("Failed to find the nonce value on the page.")
                return "request_error"

            nonce_value = nonce_input["value"]

            payload = {
                "username": email,
                "password": "dummy_password",
                "woocommerce-login-nonce": nonce_value,
                "_wp_http_referer": "/my-account-2/",
                "login": "Влизане"
            }

            async with session.post(LOGIN_POST_URL, data=payload, headers=HEADERS) as login_response:
                if login_response.status != 200:
                    print("Request error: Unable to complete the login request.")
                    return "request_error"

                response_text = await login_response.text()

                if "Непознат имейл адрес" in response_text:
                    return "user_does_not_exist"
                elif "Паролата, която въведохте за имейл адреса" in response_text:
                    return "user_exists"
                else:
                    return "request_error"

        except aiohttp.ClientError as e:
            print(f"Request failed: {str(e)}")
            return "request_error"
