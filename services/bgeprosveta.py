import requests

def check_username_registration(email):
    login_url = 'https://auth.e-prosveta.bg/user/auth'
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'Origin': 'https://bg.e-prosveta.bg',
        'Referer': 'https://bg.e-prosveta.bg/',
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json',
        'X-Device-Hash': '13716305190ae453f6317dde9d18eda83cc971519428c4ba62edbe422ef67360',
        'X-Viewer-Lang': 'bg'
    }
    
    payload = {
        'email': email,
        'password': '321321321',
        'device_hash': '13716305190ae453f6317dde9d18eda83cc971519428c4ba62edbe422ef67360'
    }

    try:
        response = requests.post(login_url, headers=headers, json=payload)

        if '"error":"wrong_email"' in response.text:
            return "user_does_not_exist"
        elif '"error":"wrong_password"' in response.text:
            return "user_exists"
        else:
            return "request_error"
        
    except requests.RequestException as e:
        print("Request failed:", str(e))
        return "request_error"