from ExpenseCategory import ExpenseCategory
class Other(ExpenseCategory):
    
    def __init__(self, money):
        super().__init__(money)
        self._name="other"