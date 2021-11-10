import Clothes
import Food
import Gifts
import Other
import Salary
import Transport
import RandomMoney
import Budget

def get_opinion():
    option1=input("Doriti sa introduceti expense sau income? ")
    if option1.lower()=="expense":
        option2=input("Doriti sa introduceti food, clothes, transport, sau other? ")
        if option2.lower()=="food" or option2.lower()=="clothes" or option2.lower()=="transport" or option2.lower()=="other":
            money=float(input("Suma cheltuita pe categoria aleasa este: "))
    elif option1.lower()=="income":
        option2=input("Doriti sa introduceti salary, gifts sau randommoney: ")
        if option2.lower()=="salary" or option2.lower()=="gifts" or option2.lower()=="randommoney":
            money=float(input("Suma primita din categoria aleasa: "))
    else:
        return None, None, None
    return option1, option2, money

def ClassFactory(op1, op2, mny):
    if op1.lower()=="expense":
        if op2.lower()=="transport":
            return Transport.Transport(mny)
        if op2.lower()=="food":
            return Food.Food(mny)
        if op2.lower()=="clothes":
            return Clothes.Clothes(mny)
        if op2.lower()=="other":
            return Other.Other(mny)
        else:
            pass
    elif op1.lower()=="income":
        if op2.lower()=="salary":
            return Salary.Salary(mny)
        elif op2.lower()=="gifts":
            return Gifts.Gifts(mny)
        elif op2.lower()=="randommoney":
            return RandomMoney.RandomMoney(mny)
        else:
            pass
    else:
        pass
if __name__=="__main__":
        transp=Transport.Transport(5)
        print(transp)
        clth=Clothes.Clothes(10)
        print(clth)
        fd=Food.Food(20)
        print(fd)
        slry=Salary.Salary(100)
        print(slry)
        bdg=Budget.Budget()
        bdg.addChange(transp)
        bdg.addChange(slry)
        bdg.addChange(clth)
        bdg.addChange(fd)
        bdg.applyChanges()
        print(f"Dupa Toate chestiile am {bdg.money} lei")
        opinion=input("Doriti sa adaugati ceva? Da sau Nu?: ")
        while opinion=="Da":
            op1,op2,mon=get_opinion()
            if op1 is not None:
                additional_class=ClassFactory(op1,op2,mon)
                bdg.addChange(additional_class)
                bdg.applyChanges()
                print(f"Acum aveti {bdg.money} bani")
                opinion=input("Doriti sa mai introduceti ceva? Da sau Nu?: ")


