import requests

def check_ftt_username_registration(username, password):
    session = requests.Session()
    login_url = 'https://ftt.uni-sz.bg/international-students/login.php'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Origin': 'https://ftt.uni-sz.bg',
        'Referer': 'https://ftt.uni-sz.bg/international-students/login.php',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    payload = {
        'username': username,
        'password': password,
    }

    try:
        response = session.post(login_url, headers=headers, data=payload)
        response.raise_for_status()

        print(f"Response Status Code: {response.status_code}")

        if "No account found with this username" in response.text:
            return "user_does_not_exist"
        elif "Wrong password" in response.text or "wrong password" in response.text:
            return "user_exists"
        else:
            print("Unexpected response content:")
            print(response.text)
            return "request_error"

    except requests.RequestException as e:
        print("Request failed:", str(e))
        return "request_error"
