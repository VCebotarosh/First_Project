from ExpenseCategory import ExpenseCategory
class Food(ExpenseCategory):
    
    def __init__(self, money):
        super().__init__(money)
        self._name="food"