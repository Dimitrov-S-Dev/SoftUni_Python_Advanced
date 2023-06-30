from typing import List


class EmailValidator:
    def __init__(self, min_length: int, mails: List[str], domains: List[str]):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name: str) -> bool:
        return len(name) >= self.min_length

    def __is_mail_valid(self, mail: str) -> bool:
        return mail in self.mails

    def __is_domain_valid(self, domain: str) -> bool:
        return domain in self.domains

    def validate(self, email: str) -> bool:
        full_mail = email.split("@")
        username = full_mail[0]
        mail, domain = full_mail[1].split(".")
        is_name_valid = self.__is_name_valid(username)
        is_domain_valid = self.__is_domain_valid(domain)
        is_mail_valid = self.__is_mail_valid(mail)
        return all([is_name_valid, is_mail_valid, is_domain_valid])
