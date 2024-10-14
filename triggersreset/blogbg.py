import requests
from bs4 import BeautifulSoup

# URL of the form
url = 'https://blog.bg/forgotten.php'


def check_username_registration(email):
    # Payload for the POST request
    payload = {
        'un': email,
        'pw': '321321321',
        'pw2': '321321321'
    }

    # Send the POST request
    response = requests.post(url, data=payload)

    if response.status_code == 200:
        # Parse the response content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the error message
        error_msg = soup.find('div', class_='msg error')

        if error_msg:
            error_text = error_msg.get_text().strip()
            if "Този e-mail адрес не е бил използван при регистрация." in error_text:
                return 'user_not_existing'
            else:
                return 'unspecified_error'
        else:
            return 'user_exists'
    else:
        return 'unspecified_error'


# List of emails to test
emails_to_test = [
    'jakalito@abv.bg',
    'example1@example.com',
    'testuser@example.com',
    'nonexistent@example.com'
]

# Test each email
for email in emails_to_test:
    status = check_username_registration(email)
    print(f'Email: {email} - Status: {status}')
