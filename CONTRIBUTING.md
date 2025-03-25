# Contributing to OpenEcho

Thank you for your interest in contributing to OpenEcho – an email registration checker for popular Bulgarian websites.

## How to Contribute

- **Fork the Repository:** Create a fork and clone it to your local development environment.
- **Create a Branch:** Use a descriptive branch name for your changes, e.g., `feature/add-new-scraper`.
- **Make Your Changes:** 
  - For new scrapers, follow the naming and implementation guidelines in the README.
  - Ensure scrapers are asynchronous and return one of the statuses:
    - `user_exists`
    - `user_does_not_exist`
    - `captcha_error`
    - `request_error`
- **Testing:** Test your code changes thoroughly. Write tests if applicable.
- **Code Style:** Follow PEP8 conventions and keep your changes minimal and modular.

## Pull Request Process

- Submit a pull request (PR) with a clear description of your changes.
- Ensure that all tests pass.
- Reference any issues that your PR closes or addresses.
- Maintain existing conventions, using concise commit messages.

## Bug Reports & Feature Requests

- Please open an issue in the GitHub issue tracker for any bugs or feature requests.
- Provide as much detail as possible.

Thank you for contributing to OpenEcho!
