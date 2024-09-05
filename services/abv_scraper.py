import requests

def check_username_registration(username):
    base_url = 'https://passport.abv.bg/app/profiles/validateename'

    params = {
        'id' : username,
        'fname': '',
        'lname': '',
        'byear': ''
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status() # Check for HTTP errors

        response_text = response.text

        if '<result>info.showcaptcha</result>' in response_text:
            print("Captcha required. Unable to proceed.")
            return None

        if '<result>info.occupied</result>' in response_text:
            return True
        elif '<result>info.free</result>' in response_text:
            return False
        else:
            return None

    except requests.exceptions.RequestException as e:
        print(f"An error occured: {e}")
        return None

username_to_check = 'jakalito' # Replace with the actual username you want to check
is_registered = check_username_registration(username_to_check)

if is_registered is None:
    print("Could not determine the registration status.")
elif is_registered:
    print(f"The username {username_to_check} is already registered.")
else:
    print(f"The username {username_to_check} is not registered.")