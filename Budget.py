class Budget:
    def __init__(self):
        self.money=0
        self.change_list={"expenses":[], "incomes":[]}
    
    def addChange(self, change):
        if change._type=="expense":
            self.change_list["expenses"].append(change)
        else:
            self.change_list["incomes"].append(change)
    
    def applyChanges(self):
        for expense in self.change_list["expenses"]:
            self.money-=expense.quantify()
        for income in self.change_list["incomes"]:
            self.money+=income.quantify()
        self.change_list={"expenses":[], "incomes":[]}