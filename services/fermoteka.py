import requests

def check_user_status(email):
    url = "https://fermoteka.bg/login"

    payload = {
        "Email": email,
        "Password": "321321321",
        "RememberMe": "false"
    }

    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "fermoteka.bg",
        "Origin": "https://fermoteka.bg",
        "Referer": "https://fermoteka.bg/login",
        "Sec-CH-UA": '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
        "Sec-CH-UA-Mobile": "?0",
        "Sec-CH-UA-Platform": '"Windows"',
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
    }

    cookies = {
        "style": "red",
        "Nop.customer": "955fd78a-9c9e-4c9a-8a5d-0247d2bc0043"
    }

    try:
        response = requests.post(url, data=payload, headers=headers, cookies=cookies)

        response_text = response.text

        if "Няма такъв потребител" in response_text:
            return "user_does_not_exist"
        elif "Данните са невалидни" in response_text:
            return "user_exists"
        else:
            return "request_error"

    except requests.RequestException as e:
        print(f"Request failed: {str(e)}")
        return "request_error"