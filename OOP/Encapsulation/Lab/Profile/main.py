class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username_value):
        if len(username_value) not in range(5, 16):
            raise ValueError("The username must be between 5 and 15"
                             " characters.")
        self.__username = username_value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, pass_value):
        has_uppercase = len([c for c in pass_value if c.isupper()]) > 0
        has_digit = len([d for d in pass_value if d.isdigit()]) > 0
        has_min_length = len(pass_value) >= 8

        if not has_uppercase or not has_digit or not has_min_length:
            raise ValueError("The password must be 8 or more characters "
                             "with at least 1 digit and 1 uppercase letter.")
        self.__password = pass_value

    def __str__(self):
        return f'You have a profile with username: "{self.__username}" ' \
               f'and password: {"*" * len(self.__password)}'

