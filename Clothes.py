from ExpenseCategory import ExpenseCategory
class Clothes(ExpenseCategory):
    
    def __init__(self, money):
        super().__init__(money)
        self._name="clothes"