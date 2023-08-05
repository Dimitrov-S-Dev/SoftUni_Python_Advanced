from project.clients.adult import Adult
from project.loans.base_loan import BaseLoan


class MortgageLoan(BaseLoan):
    def __init__(self):
        super().__init__(3.5, 50000.0)

    @property
    def available_for(self):
        return Adult.__name__

    @property
    def increase_rate_percent(self):
        return 0.5
