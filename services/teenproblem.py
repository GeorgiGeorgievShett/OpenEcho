import requests
from bs4 import BeautifulSoup


def check_username_teenproblem(email: str) -> str:
    url = 'https://www.teenproblem.net/users/login.html?redirect=/users/register/step3.html'

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://www.teenproblem.net',
        'Referer': 'https://www.teenproblem.net/users/login.html?redirect=/users/register/step3.html',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    }

    payload = {
        'redirect': '/users/register/step3.html',
        'data[email]': email,
        'data[password]': '321321321',
        'login_btn': ''
    }

    response = requests.post(url, headers=headers, data=payload)
    response.raise_for_status()


    soup = BeautifulSoup(response.text, 'html.parser')

    if soup.find('div', class_='msg not_correct') and 'Грешна парола' in response.text:
        return 'user_exists'
    elif 'Несъществуващ акаунт' in response.text:
        return 'user_does_not_exist'
    else:
        return 'unknown_response'
