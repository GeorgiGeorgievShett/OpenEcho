import asyncio
from utils.validation import validate_email, InvalidEmailError
from utils.logo import display_logo
from utils.scrapers import SCRAPERS


async def check_all_sites(email):
    """
    Asynchronously checks all sites for the provided email.
    """
    try:
        validate_email(email)
    except InvalidEmailError as e:
        print(str(e))
        return False

    tasks = []
    for site_name, scraper in SCRAPERS.items():
        tasks.append(check_site(email, scraper, site_name))

    results = await asyncio.gather(*tasks)

    for result in results:
        if result:
            display_site_status(*result)

    return True


async def check_site(email, scraper, site_name):
    """
    Executes an individual scraper asynchronously and returns the result.
    """
    try:
        email_display = email
        result = await scraper(email)
        return result, email_display, site_name
    except Exception as e:
        print(f"Error checking {email} on {site_name}: {str(e)}")
        return None


def display_site_status(result, email_display, site_name):
    """
    Displays the status of a site based on the scraper's result.
    """
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

    async def main():
        while True:
            email = input("Enter email address: ")
            if await check_all_sites(email):
                break

    asyncio.run(main())
