import requests


def check_username_registration(email):
    # URL for checking email registration
    url = 'https://www.plovdiv24.bg/js/nkselect.php'

    # Parameters for the request
    params = {
        'switch': 'check',
        'userid': '',
        'obekt': 'regemail',
        'value': email
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()

        response_text = response.text

        # Check for specific text in the response to determine email status
        if 'Този e-mail вече е регистриран!' in response_text:
            return "user_exists"
        elif 'hasemail=1' in response_text:
            return "user_does_not_exist"
        else:
            return "unknown_response"

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return "request_error"

