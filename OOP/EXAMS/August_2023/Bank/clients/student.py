from OOP.EXAMS.August_2023.Bank.clients.base_client import BaseClient


class Student(BaseClient):
    def __init__(self, name: str, client_id: str, income: float):
        super().__init__(name, client_id, income, 2.0)

    @property
    def increase_interest_percent(self):
        return 1.0
