from OOP.EXAMS.August_2023.Bank.clients.student import Student
from OOP.EXAMS.August_2023.Bank.loans.base_loan import BaseLoan


class StudentLoan(BaseLoan):
    def __init__(self):
        super().__init__(1.5, 2000.0)

    @property
    def available_for(self):
        return Student.__name__

    @property
    def increase_rate_percent(self):
        return 0.2
