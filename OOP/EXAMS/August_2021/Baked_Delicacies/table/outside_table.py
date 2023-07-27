from project.table.table import Table


class OutsideTable(Table):
    def __init__(self, table_number: int, capacity: int):
        super().__init__(table_number, capacity)

    def min_number(self):
        return 51

    def max_number(self):
        return 100

    def error_message(self):
        return f"Outside table's number must be between 51 and 100 inclusive!"
        
    
    