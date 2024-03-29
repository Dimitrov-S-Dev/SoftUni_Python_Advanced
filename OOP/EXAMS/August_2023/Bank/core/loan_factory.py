from OOP.EXAMS.August_2023.Bank.loans.mortgage_loan import MortgageLoan
from OOP.EXAMS.August_2023.Bank.loans.student_loan import StudentLoan


class LoanFactory:
    VALID_TYPES = {"StudentLoan": StudentLoan, "MortgageLoan": MortgageLoan}

    def create_loan(self, loan_type):
        if loan_type not in self.VALID_TYPES:
            raise ValueError("Invalid loan type!")
        return self.VALID_TYPES[loan_type]()
