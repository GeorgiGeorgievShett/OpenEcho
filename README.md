# OpenEcho

**OpenEcho** is a tool designed to check the registration of email addresses across a range of popular bulgarian websites. Inspired by similar tools like [holehe](https://github.com/AnonymouX/holehe), OpenEcho provides a streamlined way to verify if an email address is associated with accounts on various online platforms.


![Project Logo](services/images/openechologo.jpg)

![GitHub all releases](https://img.shields.io/github/downloads/GeorgiGeorgievShett/OpenEcho/total?color=blue&style=flat-square)

**Want to donate?**

BTC Wallet: bc1q37200rzvzpqlumqe8vctcr6vzakuwgmxk3wa3x

Monero Wallet: 861hzaFiGHuHzFsVbuk6zEj6uecBp9k38ecg8vQeVNN45VR6NL2fYvg1fSiYRhnDuYPALcWRBsHzMgVy652iVxJk3biTQfY

## Features

- **Email Address Verification**: Quickly check if an email address is registered on a wide array of popular websites.
- **Extensive Coverage**: Includes a large list of commonly used websites to ensure comprehensive checks.
- **User-Friendly Interface**: Simple command-line interface for easy use and integration into workflows.
- **Open Source**: Fully open-source, allowing for community contributions and transparency.

## Installation

To get started with OpenEcho, follow these steps:

Clone the repository:
**git clone https://github.com/GeorgiGeorgievShett/OpenEcho**

Navigate to the project directory:
**cd OpenEcho**

Install the necessary dependencies:
**pip install -r requirements.txt**

## Usage
Run OpenEcho with the following command:

**python main.py**


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

Import Your New Scraper: Fork the repository and build your scraper, make sure it is asynchronous and follows our output conventions.
Then update the utils.scrapers.py file with your scraper, keep the last ones for modified outputs like email to username.

Follow Output Conventions:
Ensure your scraper function handles responses and errors according to the defined output statuses.
Return one of the four statuses (user_exists, user_does_not_exist, captcha_error, or request_error) based on the site's response.

Testing:
Test your scraper thoroughly to confirm it behaves correctly and matches the expected output formats.

If you would like to contribute to the project feel free to make a pull request.
=======
