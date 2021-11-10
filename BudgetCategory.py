class BudgetCategory:
    
    def __init__(self, money):
        self.money=money
        self._name=""
        self._type=""

    def quantify(self):
        return self.money

    def __repr__(self):
        return f"[{self._type.title()}] {self._name.title()} : {self.money}"


    
