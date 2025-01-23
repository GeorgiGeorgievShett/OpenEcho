from utils.validation import validate_email, InvalidEmailError
from utils.logo import display_logo
from utils.email_modifier import email_name_modifier
from utils.scrapers import SCRAPERS

def check_all_sites(email):
        try:
            validate_email(email)
        except InvalidEmailError as e:
            print(str(e))
            return False
        
        for site_name, scraper in SCRAPERS.items():
            result, email_display = email_name_modifier(scraper, email, site_name)
            display_site_status(result, email_display, site_name)

        return True

def display_site_status(result, email_display, site_name):
    """Handles the display logic based on the result of the scraper."""
    if result == "user_exists":
        print(f"🔴 {email_display} is already registered on {site_name}.")
    elif result == "user_does_not_exist":
        print(f"🟢 {email_display} is available on {site_name}.")
    elif result == "captcha_error":
        print(f"⚠️ Captcha required on {site_name}. Unable to proceed.")
    elif result == "request_error":
        print(f"🔄 Error checking {email_display} on {site_name}. Rate limit or connection error.")
    else:
        print(f"❓ Unknown error for {email_display} on {site_name}.")  


if __name__ == "__main__":
    display_logo()

    while True: 
        email = input("Enter email address: ")
        if check_all_sites(email):
            break
