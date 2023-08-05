from abc import ABC, abstractmethod


class BaseLoan(ABC):
    def __init__(self, interest_rate: float, amount: float):
        self.interest_rate = interest_rate
        self.amount = amount
        
    @property
    @abstractmethod
    def available_for(self):
        pass

    @property
    @abstractmethod
    def increase_rate_percent(self):
        pass

    def increase_interest_rate(self):
        self.interest_rate += self.increase_rate_percent
