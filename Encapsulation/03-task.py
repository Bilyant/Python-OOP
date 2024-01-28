class Profile:
    """
    username: str - the username should be between 5 and 15 characters (inclusive).
    If it is not, raise a ValueError with the message
    "The username must be between 5 and 15 characters."

    password: str - the password must be at least 8 characters long;
    it must contain at least one upper case letter and at least one digit.
    If it does not, raise a ValueError with the message
    "The password must be 8 or more characters with at least 1 digit and 1 uppercase letter."

    """
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if len(value) < 5 or len(value) > 15:
            raise ValueError('The username must be between 5 and 15 characters.')
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        have_upper_chars = any([True for ch in value if ch.isupper()])
        have_digits = any([True for ch in value if ch.isdigit()])
        if len(value) < 8 or not have_upper_chars or not have_digits:
            raise ValueError('The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.')
        self.__password = value

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'


profile_with_invalid_password = Profile('My_username', 'My-password')
