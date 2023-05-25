from Custom_Exceptions import MustContainAtSymbolError, NameTooShortError, \
    InvalidDomainError

valid_domains = [".com", ".bg", ".org", ".net"]

while True:
    command = input()
    if command == "End":
        break

    email_parts = command.split("@")
    if len(email_parts) != 2:
        raise MustContainAtSymbolError("Email must contain @")

    name, domain_name = email_parts

    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    domain = f".{domain_name.split('.')[1]}"
    if domain not in ["com", ".bg", "org", "net"]:
        raise InvalidDomainError(f"Domain must be one of the following:"
                                 f" {', '.join(valid_domains)}")
