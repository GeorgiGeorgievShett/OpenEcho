import requests

def simulate_burgas24_login(email, password="generic_password"):
    login_url = 'https://users.burgas24.bg/login.html'
    
    # Headers to mimic a real browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        'Referer': 'http://www.burgas24.bg/',  
    }
    
    # Payload for login attempt (form data)
    payload = {
        'loginemail': email,
        'loginpass': password,  # Use the default or provided password
        'urlref': 'http://www.burgas24.bg/'  
    }

    session = requests.Session()

    try:
        # Send POST request to Burgas24 login URL with form data
        response = session.post(login_url, headers=headers, data=payload)
        response.raise_for_status()  

        # Check for specific messages in the response
        if "Грешна парола!" in response.text:
            return "user_exists"  
        elif "Няма регистрация с посочения email/потребителско име!" in response.text:
            return "user_does_not_exist"  
        elif "забравена парола" in response.text or "Invalid" in response.text:
            return "login_failed"  
        else:
            return "unknown_response"
        
    except requests.RequestException as e:
        print(f"Request error: {e}")
        return "request_error"