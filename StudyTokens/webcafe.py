"""import requests
from bs4 import BeautifulSoup

def get_token(session):
    response = session.get("https://webcafe.bg/login")
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        token_element = soup.find('input', {'name': '_token'})
        if token_element:
            return token_element.get('value')
    return None

def check_user_exists(email, password):
    login_url = "https://webcafe.bg/login"
    session = requests.Session()

    # Retrieve the CSRF token
    token = get_token(session)
    if not token:
        print("Failed to retrieve token.")
        return

    print(f"Token: {token}")

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://webcafe.bg',
        'Referer': 'https://webcafe.bg/login',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8'
    }

    data = {
        '_token': token,
        'remember': '1',
        'email': email,
        'password': password
    }

    # Perform login request
    response = session.post(login_url, headers=headers, data=data, allow_redirects=True)

    print(f"Login Response Status Code: {response.status_code}")
    print(f"Response Headers: {response.headers}")
    print(f"Response Text: {response.text[:2000]}")  # Print the first 2000 characters for more insight

    if "Неуспешно удостоверяване на потребител." in response.text:
        return "User does not exist"
    elif "Login" in response.text:  # Or any other message indicating login success
        return "User exists"
    else:
        return "Login failed, status code: {}".format(response.status_code)

# Example usage
email = ""
password = ""
result = check_user_exists(email, password)
print(result)
"""