import re
from services import plovdiv24, mailbg, techoffnews, econt, abv_scraper, sportal, arenabg, pomagalo, teenproblem
from services.dnevnik import check_dnevnik_user_registration
from services.burgas24 import simulate_burgas24_login
from services.varna24 import simulate_varna24_login
from services.mediapool import check_mediapool_email_registration

class InvalidEmailError(Exception):
    """Custom exception for invalid email addresses."""

    def __init__(self, email):
        self.email = email
        self.message = f"The email '{self.email}' is invalid. Please enter a valid email address."
        super().__init__(self.message)


def validate_email(email: str, allowed_domains: list) -> None:
    """Validate that the email ends with a valid domain."""
    # Regular expression to check if the email is valid
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, email):
        raise InvalidEmailError(email)

    # Check if the email ends with one of the allowed domains
    if not any(email.endswith(domain) for domain in allowed_domains):
        raise InvalidEmailError(email)


def display_logo():
    logo = """
     ██████╗ ██████╗░███████╗███╗░░██╗███████╗░█████╗░██╗░░██╗ ██████╗ 
    ██╔═══██╗██╔══██╗██╔════╝████╗░██║██╔════╝██╔══██╗██║░░██║██╔═══██╗
    ██║██╗██║██████╔╝█████╗░░██╔██╗██║█████╗░░██║░░╚═╝███████║██║██╗██║
    ██║██║██║██╔═══╝░██╔══╝░░██║╚████║██╔══╝░░██║░░██╗██╔══██║██║██║██║
    ╚█║████╔╝██║░░░░░███████╗██║░╚███║███████╗╚█████╔╝██║░░██║╚█║████╔╝
     ╚╝╚═══╝ ╚═╝░░░░░╚══════╝╚═╝░░╚══╝╚══════╝░╚════╝░╚═╝░░╚═╝ ╚╝╚═══╝ 

    """
    print(logo)
    print("Welcome to OpenEcho - Email Registration Checker for popular Bulgarian websites.")
    print("-------------------------------------------------\n")


def check_all_sites(email):
    allowed_domains = ['@abv.bg', '@gmail.com']  # Specify allowed domains

    try:
        validate_email(email, allowed_domains)  # Validate the email
    except InvalidEmailError as e:
        print(str(e))  # Print the error message if email is invalid
        return False  # Indicate invalid email

    print(f"\nChecking availability for: {email}")

    # Dictionary that maps each scraper to its corresponding website name
    scrapers = {
        "ABV.bg": abv_scraper.check_username_registration,
        "Plovdiv24.bg": plovdiv24.check_username_registration,
        "Mail.bg": mailbg.check_username_registration,
        "Offmedia.bg": techoffnews.check_username_registration,
        "Econt.com": econt.check_username_registration,
        "Sportal.bg": sportal.check_username_registration,
        "Arenabg.com": arenabg.check_username_arenabg,
        "Pomagalo.com": pomagalo.check_username_pomagalo,
        "Teenproblem.net": teenproblem.check_username_teenproblem,
        "Dnevnik.bg": check_dnevnik_user_registration,
        "Burgas24.bg": simulate_burgas24_login,
        "Varna24.bg": simulate_varna24_login,
        "Mediapool.bg": check_mediapool_email_registration,
    }

    # Loop through each scraper, testing the email/username
    for site_name, scraper in scrapers.items():
        if site_name == "Mail.bg":
            # Show the modified email (transformed for mail.bg) in the output
            modified_email = email.split('@')[0] + '@mail.bg'
            result = scraper(modified_email)
            email_display = modified_email  # Show modified email for Mail.bg
        else:
            result = scraper(email)
            email_display = email  # Show the original email for other sites

        # Display the result with the website name
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

    return True  # Indicate that the email check was successful


if __name__ == "__main__":
    display_logo()

    while True:  # Loop until a valid email is provided
        email = input("Enter email address: ")
        if check_all_sites(email):
            break  # If the check is successful, exit the loop
