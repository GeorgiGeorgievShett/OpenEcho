# OpenEcho

**OpenEcho** is a tool designed to check the registration of email addresses across a range of popular bulgarian websites. Inspired by similar tools like [holehe](https://github.com/AnonymouX/holehe), OpenEcho provides a streamlined way to verify if an email address is associated with accounts on various online platforms.

## Features

- **Email Address Verification**: Quickly check if an email address is registered on a wide array of popular websites.
- **Extensive Coverage**: Includes a large list of commonly used websites to ensure comprehensive checks.
- **User-Friendly Interface**: Simple command-line interface for easy use and integration into workflows.
- **Open Source**: Fully open-source, allowing for community contributions and transparency.

## Installation

To get started with OpenEcho, follow these steps:

Clone the repository:
git clone https://github.com/GeorgiGeorgievShett/OpenEcho

Navigate to the project directory:
cd OpenEcho

Install the necessary dependencies:
pip install -r requirements.txt

## Usage
Run OpenEcho with the following command:

python main.py


## Rules and Coding Standards
Adding a New Scraper to OpenEcho
To add a new scraper to OpenEcho, follow these steps to ensure consistency with existing scrapers:

**Create a New Scraper Module:**

**File Naming:** Use a descriptive name for the file, e.g., newsite.py.
Function Implementation: Implement a function  **___check_email____"enter website name here"** (or similar) in your module. This function should take an email as input and return one of the following values:

**user_exists**

**user_does_not_exist**

**captcha_error**

**request_error**



**Updating main.py:**

Import Your New Scraper: Add an import statement for your new scraper at the beginning of main.py.
Add to Scraper Dictionary: Update the scrapers dictionary in the check_all_sites function to include your new site and its corresponding function.
Follow Output Conventions:

Ensure your scraper function handles responses and errors according to the defined output statuses.
Return one of the four statuses (user_exists, user_does_not_exist, captcha_error, or request_error) based on the site's response.
Testing:

Test your scraper thoroughly to confirm it behaves correctly and matches the expected output formats.

