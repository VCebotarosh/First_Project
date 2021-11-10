from IncomeCategory import IncomeCategory
class RandomMoney(IncomeCategory):

    def __init__(self, money):
        super().__init__(money)
        self._name="randommoney"