from OpenEcho.openecho.services import plovdiv24, mailbg, techoffnews, econt, abv_scraper, sportal, arenabg, pomagalo


# Import other scrapers here

def check_all_sites(email):
    print(f"Checking availability for: {email}")

    # Dictionary that maps each scraper to its corresponding website name
    scrapers = {
        "ABV.bg": abv_scraper.check_username_registration,
        "Plovdiv24.bg": plovdiv24.check_username_registration,
        "Mail.bg": mailbg.check_username_registration,
        "Tech Off News": techoffnews.check_username_registration,
        "Econt": econt.check_username_registration,
        "Sportal": sportal.check_username_registration,
        "Arenabg": arenabg.check_username_arenabg,
        "Pomagalo": pomagalo.check_username_pomagalo
        # "Site3.com": site3_scraper.check_username_registration,
    }

    # Loop through each scraper, testing the email/username
    for site_name, scraper in scrapers.items():
        result = scraper(email)
        print(f"\nTesting {email} on {site_name}. Result: {result}")


        # Display the result with the website name
        if result == "user_exists":
            print(f"🔴 {email} is already registered on {site_name}.")
        elif result == "user_does_not_exist":
            print(f"🟢 {email} is available on {site_name}.")
        elif result == "captcha_error":
            print(f"⚠️ Captcha required on {site_name}. Unable to proceed.")
        elif result == "request_error":
            print(f"🔄 Error checking {email} on {site_name}. Rate limit or connection error.")
        else:
            print(f"❓ Unknown error for {email} on {site_name}.")


if __name__ == "__main__":
    email = ''  # Get email from command-line arguments
    check_all_sites(email)
