import requests
from bs4 import BeautifulSoup

def check_username_registration(email):
    session = requests.Session()
    login_page_url = 'https://jobs.cyberclub.bg/Account/Login'
    login_url = 'https://jobs.cyberclub.bg/Account/Login'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',  # Expecting HTML now
        'Referer': login_page_url,
        'Origin': 'https://jobs.cyberclub.bg',
    }

    try:
        response = session.get(login_page_url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        token_input = soup.find('input', {'name': '__RequestVerificationToken'})
        if not token_input or not token_input['value']:
            print("Unable to find the __RequestVerificationToken.")
            return "request_error"

        verification_token = token_input['value']
        print(f"Retrieved Verification Token: {verification_token}")

        payload = {
            'Email': email,
            '__RequestVerificationToken': verification_token,
        }

        response = session.post(login_url, headers=headers, data=payload)
        response.raise_for_status()

        if '/Account/Register?lang=EN' in response.text:
            return "user_does_not_exist"
        elif '/Account/Login?lang=EN' in response.text:
            return "user_exists"
        else:
            return "request_error"

    except requests.RequestException as e:
        return "request_error"