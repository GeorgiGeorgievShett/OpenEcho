import requests
import json

def check_username_registration(email):
    # URL for the login page
    url = "https://login.econt.com/rpc.php"

    # Headers Information
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.64 Safari/537.36'
    }

    # Payload data with a dummy password
    payload = {
        "id": 1,
        "jsonrpc": "2.0",
        "method": "Authentication.login",
        "params": {
            "username": email,
            "password": "dummyPassword123",
            "login_for_password_change": 0
        }
    }

    # Send the POST request
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    # Check the response
    response_json = response.json()

    # Determine if the email is registered
    if "Липсва профил с този имейл" in response_json.get('error', {}).get('message', ''):
        return "user_does_not_exist"
    elif "Моля, въведете валидна парола." in response_json.get('error', {}).get('message', ''):
        return "user_exists"
    else:
        return "unknown_response"