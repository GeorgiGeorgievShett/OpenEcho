import requests

def check_username_registration(email):
    username = email.split('@')[0]

    base_url = 'https://passport.abv.bg/app/profiles/validateename'

    params = {
        'id': username,
        'fname': '',
        'lname': '',
        'byear': ''
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()

        response_text = response.text

        if '<result>info.showcaptcha</result>' in response_text:
            return "captcha_error"
        if '<result>info.occupied</result>' in response_text:
            return "user_exists"
        elif '<result>info.free</result>' in response_text:
            return "user_does_not_exist"
        else:
            return "unknown_error"

    except requests.exceptions.RequestException:
        return "request_error"
