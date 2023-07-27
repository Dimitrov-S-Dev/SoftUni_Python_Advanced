from OOP.EXAMS.August_2021.Baked_Delicacies.table.table import Table


class InsideTable(Table):
    def __init__(self, table_number: int, capacity: int):
        super().__init__(table_number, capacity)

    def min_number(self):
        return 1

    def max_number(self):
        return 50

    def error_message(self):
        return f"Inside table's number must be between 1 and 50 inclusive!"
