class InvalidEmailError(Exception):
    """Custom exception for invalid email addresses."""
    def __init__(self, email):
        self.email = email
        self.message = f"The email, '{self.email}' is invalid. Please enter a valid email."
        super().__init__(self.message)

def validate_email(email: str) -> None:
    """Validate that the email contains an '@' and '.' symbol."""
    if "@" and "." not in email:
        raise InvalidEmailError