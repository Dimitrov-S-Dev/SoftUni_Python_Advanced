from project.clients.adult import Adult
from project.clients.student import Student


class ClientFactory:
    VALID_TYPES = {"Student": Student, "Adult": Adult}

    def create_client(self, client_type, client_name, client_id, income):
        if client_type not in self.VALID_TYPES:
            raise ValueError("Invalid client type!")
        return self.VALID_TYPES[client_type](client_name, client_id, income)

