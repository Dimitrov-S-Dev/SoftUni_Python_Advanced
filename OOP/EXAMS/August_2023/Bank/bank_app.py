from OOP.EXAMS.August_2023.Bank.core.client_factory import ClientFactory
from OOP.EXAMS.August_2023.Bank.core.loan_factory import LoanFactory


class BankApp:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans = []
        self.clients = []

        self.loans_granted = 0
        self.granted_sum = 0
        self.loan_factory = LoanFactory()
        self.client_factory = ClientFactory()

    def add_loan(self, loan_type: str):

        try:
            loan = self.loan_factory.create_loan(loan_type)
            self.loans.append(loan)
            return f"{loan_type} was successfully added."
        except ValueError as error:
            raise Exception(error)

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):

        try:
            client = self.client_factory.create_client(client_type, client_name, client_id, income)
        except ValueError as error:
            raise Exception(error)

        if len(self.clients) == self.capacity:
            return f"Not enough bank capacity."

        self.clients.append(client)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):

        loan = self.__find_loan_by_loan_type(loan_type)
        client = self.__find_client_by_client_id(client_id)

        if loan.available_for != client.__class__.__name__:
            raise Exception("Inappropriate loan type!")

        client.loans.append(loan)
        self.loans.remove(loan)
        self.loans_granted += 1
        self.granted_sum += loan.amount
        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id: str):

        client = self.__find_client_by_client_id(client_id)
        if client is None:
            raise Exception("No such client!")

        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."
        # first_upload

    def increase_loan_interest(self, loan_type: str):

        changed_loans = list(filter(lambda x: x.__class__.__name__ == loan_type, self.loans))

        for loan_ in changed_loans:
            loan_.increase_interest_rate()

        return f"Successfully changed {len(changed_loans)} loans."

    def increase_clients_interest(self, min_rate: float):

        changed_clients_rate = list(filter(lambda c: c.interest < min_rate, self.clients))

        for client in changed_clients_rate:
            client.increase_clients_interest()

        return f"Number of clients affected: {len(changed_clients_rate)}."
        # second_upload

    def get_statistics(self):
        output = f"Active Clients: {len(self.clients)}" + "\n"

        total_clients_income = sum(c.income for c in self.clients)
        output += f"Total Income: {total_clients_income:.2f}" + "\n"

        output += f"Granted Loans: {self.loans_granted}, Total Sum: {self.granted_sum:.2f}" + "\n"
        output += f"Available Loans: {len(self.loans)}, Total Sum: {sum(l.amount for l in self.loans):.2f}" + "\n"
        avg_client_interest_rate = 0 if len(self.clients) == 0 else sum(client.interest for client in self.clients) / len(self.clients)

        output += f"Average Client Interest Rate: {avg_client_interest_rate:.2f}"

        return output

    def __find_loan_by_loan_type(self, loan_type):
        for loan in self.loans:
            if loan.__class__.__name__ == loan_type:
                return loan
        return None

    def __find_client_by_client_id(self, client_id):
        for client in self.clients:
            if client.client_id == client_id:
                return client
        return None
