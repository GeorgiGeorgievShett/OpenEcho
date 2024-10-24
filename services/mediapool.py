import requests
from bs4 import BeautifulSoup

def check_mediapool_email_registration(email):
    """
    Check if an email is already registered on Mediapool.bg by submitting a registration attempt.
    This version includes extraction of the CSRF _nonce token before submitting the form.
    """
    registration_url = 'https://www.mediapool.bg/users/reg'  # Registration URL
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        'Referer': 'https://www.mediapool.bg/',
    }
    
    session = requests.Session()

    try:
        # First request to get the CSRF token (_nonce)
        response = session.get(registration_url, headers=headers)
        
        
        soup = BeautifulSoup(response.content, 'html.parser')
        nonce_input = soup.find('input', {'name': '_nonce'})
        
        if nonce_input and 'value' in nonce_input.attrs:
            nonce_value = nonce_input['value']
        else:
            return "nonce_not_found"

        payload = {
            '_nonce': nonce_value, 
            'username': 'Martina',  
            'email': email, 
            'password': 'random_password',  
            'password1': 'random_password',  
            'terms_consent': '1', 
            'newsletter_1': '1',  
        }

        # Second request: attempt registration
        registration_response = session.post(registration_url, data=payload, headers=headers)
        

        # Check for specific phrases in the response content
        if "Имейл адресът, който сте въвели, вече е регистриран в Mediapool.bg" in registration_response.text:
            return "user_exists"  # Email is already registered
        elif "невалидна заявка" in registration_response.text or "Грешка" in registration_response.text:
            return "request_error"  # If there is an issue with form submission
        else:
            return "user_does_not_exist"  # Other responses not handled

    except requests.RequestException as e:
        return "request_error"
