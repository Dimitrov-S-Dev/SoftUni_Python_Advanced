class Profile:
    min_username_length = 5
    max_username_length = 15

    min_password_length = 8
    min_uppercase_letters_count = 1
    min_digits_count = 1

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __validate_username(self, username):
        if len(username) not in range\
                   (self.min_username_length, self.min_username_length):
            raise ValueError("The username must be between 5 and 15"
                             " characters.")

    def __validate_password(self, pass_value):
        has_uppercase = len([c for c in pass_value if c.isupper()]) \
                        > self.min_uppercase_letters_count
        has_digit = len([d for d in pass_value if d.isdigit()]) \
                        > self.min_digits_count
        has_min_length = len(pass_value) >= self.min_password_length

        if not has_uppercase or not has_digit or not has_min_length:
            raise ValueError("The password must be 8 or more characters "
                             "with at least 1 digit and 1 uppercase letter.")

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        self.__validate_username(value)
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__validate_password(value)
        self.__password = value

    def __str__(self):
        return f'You have a profile with username: "{self.__username}" ' \
               f'and password: {"*" * len(self.__password)}'

