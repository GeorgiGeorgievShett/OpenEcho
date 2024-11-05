import requests


def check_username_registration(email):
    url = f"https://id.offmedia.bg/ajax/email/?email={requests.utils.quote(email)}"

    headers = {
        'Accept': 'application/json, text/javascript, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        if response.text.strip() == "OK":
            return "user_does_not_exist"
        elif response.text.strip() == "ERR":
            return "user_exists"
        else:
            return "unknown_response"

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return "request_error"