import requests

def check_username_registration(email):
    session = requests.Session()
    login_url = 'https://pragmatic.bg/wp-login.php'
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://pragmatic.bg',
        'Referer': 'https://pragmatic.bg/wp-login.php',
    }
    
    payload = {
        'log': email,
        'pwd': 'dummy_password',
        'wp-submit': 'Log In',
        'redirect_to': 'https://pragmatic.bg/wp-admin/',
        'testcookie': '1'
    }
    
    try:
        session.get(login_url, headers=headers)
        
        response = session.post(login_url, headers=headers, data=payload)
        response.raise_for_status()

        if "Unknown email address." in response.text:
            return "user_does_not_exist"
        elif "Error: The password you entered for the username" in response.text or "Error: The password you entered for the email address" in response.text:
            return "user_exists"
        else:
            return "request_error"

    except requests.RequestException as e:
        return "request_error"
