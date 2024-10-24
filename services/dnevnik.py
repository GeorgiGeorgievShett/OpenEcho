import requests

def check_dnevnik_user_registration(email):
    url = 'https://www.dnevnik.bg/user/pre-login'
    payload = {
        'login[_email]': email,
        'login[_password]': '',
        'login[_remember_me]': 1
    }

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }

    try:
        response = requests.post(url, headers=headers, data=payload)
        response.raise_for_status()  # Raise an error for bad responses

        response_data = response.json()
        if response_data.get("err_cnt") == 0:
            return "user_exists"
        elif response_data.get("err_cnt") == 1:
            return "user_does_not_exist"
        else:
            return "unknown_error"

    except requests.exceptions.RequestException:
        return "request_error"
    except ValueError:
        return "json_error"
