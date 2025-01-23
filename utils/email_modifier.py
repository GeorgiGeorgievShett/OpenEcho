def email_name_modifier(scraper, email, site_name):
    """Helper function to modify the names for certain sites."""
    if site_name == "Mail.bg":
        modified_email = email.split('@')[0] + '@mail.bg'
        email_display = modified_email
    elif site_name == "Chitanka.info":
        modified_email = email.split('@')[0]
        email_display = modified_email
    elif site_name == "ABV.bg":
        modified_email = email.split('@')[0] + '@abv.bg'
        email_display = modified_email
    else:
        modified_email = email
        email_display = email

    result = scraper(modified_email)
    return result, email_display