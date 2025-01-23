import requests

def check_username_registration(email, password="generic_password"):
    login_url = 'https://users.burgas24.bg/login.html'
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        'Referer': 'http://www.burgas24.bg/',  
    }
    
    payload = {
        'loginemail': email,
        'loginpass': password, 
        'urlref': 'http://www.burgas24.bg/'  
    }

    session = requests.Session()

    try:
        response = session.post(login_url, headers=headers, data=payload)
        response.raise_for_status()  

        if "Грешна парола!" in response.text:
            return "user_exists"  
        elif "Няма регистрация с посочения email/потребителско име!" in response.text:
            return "user_does_not_exist"  
        else:
            return "request_error"
        
    except requests.RequestException as e:
        return "request_error"