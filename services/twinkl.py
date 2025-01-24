import requests
from bs4 import BeautifulSoup

def check_username_registration(email):
    session = requests.Session()
    login_page_url = 'https://www.twinkl.bg/sign-in'
    login_url = 'https://www.twinkl.bg/user/sign-in'
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': login_page_url,
    }
    
    try:
        response = session.get(login_page_url, headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        csrf_token = soup.find('input', {'name': 'csrf'})['value']
        print(f"Retrieved CSRF Token: {csrf_token}")

        payload = {
            'username': email,
            'password': '321321321',
            'csrf': csrf_token,
            'ajax': 1,
            'captcha_response': '',
            'captcha_version': ''
        }
        
        response = session.post(login_url, headers=headers, data=payload)
        response.raise_for_status()

        print(f"Response Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")

        if "Sorry, try another email address." in response.text:
            return "user_does_not_exist"
        elif "Sorry, that wasn't the correct password." in response.text:
            return "user_exists"
        else:
            return "request_error"

    except requests.RequestException as e:
        print("Request failed:", str(e))
        return "request_error"
