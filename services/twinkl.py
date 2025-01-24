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
        
        # Print the full HTML response for debugging
        print("HTML Response:")
        print(response.text)

        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Attempt to find the CSRF token
        csrf_input = soup.find('input', {'name': 'csrf'})
        if not csrf_input:
            print("CSRF input element not found!")
            return "request_error"
        
        csrf_token = csrf_input.get('value')
        if not csrf_token:
            print("CSRF token value not found!")
            return "request_error"
        
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

if __name__ == "__main__":
    email_to_check = "hope_hope_1996@abv.bg"
    result = check_username_registration(email_to_check)
    print(f"Result: {result}")


testemail = "tetetete@abv.bg"
result = check_username_registration(testemail)
print(result)