from IncomeCategory import IncomeCategory
class Gifts(IncomeCategory):
    def __init__(self, money):
        super().__init__(money)
        self._name="gifts"