from IncomeCategory import IncomeCategory
class Salary(IncomeCategory):
    def __init__(self, money):
        super().__init__(money)
        self._name="salary"

    
    
    