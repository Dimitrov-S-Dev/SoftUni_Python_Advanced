class Account:
    def __init__(self, owner: str, amount: int = 0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")
        self._transactions.append(amount)

    @property
    def balance(self):
        return self.amount + sum(self._transactions)

    @staticmethod
    def validate_transaction(account, amount_to_add):
        if account.balance + amount_to_add < 0:
            raise ValueError("sorry cannot go in debt!")
        account.add._transaction(amount_to_add)
        return f"New balance: {account.balance}"

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}."

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    def __len__(self):
        return len(self._transactions)

    def __reversed__(self):
        return reversed(self._transactions)

    def __getitem__(self, idx):
        return self._transactions[idx]

    def __gt__(self, other):
        return self.amount > other.amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __ge__(self, other):
        return self.amount >= other.amount

    def __add__(self, other):
        new_owner = self.owner + "&" + other.owner
        new_amount = self.amount + other.amount
        new_acc = Account(new_owner, new_amount)
        new_acc._transactions = self._transactions + other._transactions
        return new_acc
