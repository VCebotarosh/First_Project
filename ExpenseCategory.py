from BudgetCategory import BudgetCategory
class ExpenseCategory(BudgetCategory):
    
    def __init__(self, money):
        super().__init__(money)
        self._type="expense"