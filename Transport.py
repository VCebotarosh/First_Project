from ExpenseCategory import ExpenseCategory
class Transport(ExpenseCategory):
    
    def __init__(self, money):
        super().__init__(money)
        self._name="transport"