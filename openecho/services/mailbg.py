import requests

def check_username_registration(email_or_username):
    # If the input is just a username or a different email, adjust it
    if '@mail.bg' not in email_or_username:
        # Strip the domain part if it's not @mail.bg
        username = email_or_username.split('@')[0]
        email = f"{username}@mail.bg"
    else:
        email = email_or_username

    encoded_email = requests.utils.quote(email)
    url = f'https://mail.bg/signup/checkuser/format/json/user/{encoded_email}'

    headers = {
        'Accept': 'application/json, text/javascript, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }

    cookies = {
        'OAID': '1234567890abcdef',  # Example value
        'current_page': 'mailbox/inbox',
        's': 'abcdef1234567890',    # Example value
        't': 'q7_w9g-42_s.e3r7.28.bg',
        'vid': '0987654321fedcba'   # Example value
    }

    try:
        response = requests.get(url, headers=headers, cookies=cookies)
        response.raise_for_status()

        # Check if response is JSON
        try:
            response_json = response.json()
        except ValueError:
            return "response_not_json"

        # Check for email registration status in response
        if response_json.get('result') is True:
            return "user_does_not_exist"
        elif response_json.get('result') is False:
            return "user_exists"
        else:
            return "unknown_response"

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return "request_error"
    except ValueError:
        return "json_error"

# Example usage
email_or_username = 'georgi'  # Can be a username or a full email address
status = check_username_registration(email_or_username)
print(status)
