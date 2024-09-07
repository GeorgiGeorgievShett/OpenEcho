import requests
from bs4 import BeautifulSoup


def check_username_arenabg(username_or_email, password):
    session = requests.Session()

    login_url = "https://arenabg.com/bg/users/signin/"
    login_data = {
        "username_or_email": username_or_email,
        "password": password
    }

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Referer": "https://arenabg.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
    }

    # Send POST request to login
    response = session.post(login_url, data=login_data, headers=headers)

    # Check if response is not a redirect (i.e., not 302)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        page_text = soup.get_text()

        # Check for potential error messages in the login response
        if 'грешна' in page_text.lower():
            return "user_exists"
        elif 'не е намерен' in page_text.lower():
            return "user_does_not_exist"
        else:
            return "Login failed for unknown reasons."
    else:
        return f"Unexpected status code: {response.status_code}"
