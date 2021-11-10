from BudgetCategory import BudgetCategory
class IncomeCategory(BudgetCategory):
    def __init__(self, money):
        super().__init__(money)
        self._type="income"

