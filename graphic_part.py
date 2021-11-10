from tkinter import font
from tkinter import *
import main_project
import Budget
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


font_large=("TimesNewRoman", 20, "bold", "underline")
font_normal=("TimesNewRoman", 14, "bold")

app=Tk()
app.title("Gestionarea Bugetului")
app.geometry("1200x650")
app.configure(background="goldenrod")

bdg=Budget.Budget()

def submt():
    values={"expense": {}, "income": {}}
    values["expense"]["transport"]=transp_value.get()
    values["expense"]["clothes"]=cloth_value.get()
    values["expense"]["food"]=food_value.get()
    values["expense"]["other"]=other_value.get()
    values["income"]["salary"]=salary_value.get()
    values["income"]["gifts"]=gift_value.get()
    values["income"]["randommoney"]=random_money_value.get()
    for key, value in values.items():
        if key=="expense":
            for key2,value2 in values["expense"].items():
                additional_class=main_project.ClassFactory(key, key2, value2)
                bdg.addChange(additional_class)
                bdg.applyChanges()
        elif key=="income":
            for key2, value2 in values["income"].items():
                additional_class=main_project.ClassFactory(key, key2, value2)
                bdg.addChange(additional_class)
                bdg.applyChanges()
    money.set("Acum am " + str(bdg.money)+" lei")

def show_statistic():
    values={"category": ["transport", "clothes", "food","other","salary","gifts","randommoney"], "amount_mny": []}
    
    values["amount_mny"].append(transp_value.get())
    values["amount_mny"].append(cloth_value.get())
    values["amount_mny"].append(food_value.get())
    values["amount_mny"].append(other_value.get())
    values["amount_mny"].append(salary_value.get())
    values["amount_mny"].append(gift_value.get())
    values["amount_mny"].append(random_money_value.get())
    
    transp_value.set("0.0")
    cloth_value.set("0.0")
    food_value.set("0.0")
    other_value.set("0.0")
    salary_value.set("0.0")
    gift_value.set("0.0")
    random_money_value.set("0.0")
    
    window=Tk()
    window.title("Statistics")
    window.geometry("600x600")
    window.configure(background="khaki")
    
    df1=DataFrame(values, columns=["category", "amount_mny"])
    figure1 = plt.Figure(figsize=(6,5), dpi=100)
    ax1 = figure1.add_subplot(111)
    chart_type = FigureCanvasTkAgg(figure1, window)
    chart_type.get_tk_widget().pack(side=LEFT, fill=BOTH)
    df1 = df1[['category','amount_mny']].groupby('category').sum()
    df1.plot(kind='bar', legend=True, ax=ax1)
    ax1.set_title('Money spend on categories')
  

transp_value=DoubleVar(app)
cloth_value=DoubleVar(app)
food_value=DoubleVar(app)
other_value=DoubleVar(app)
salary_value=DoubleVar(app)
gift_value=DoubleVar(app)
random_money_value=DoubleVar(app)

money=StringVar(app)
money.set("Acum am " +str(bdg.money)+" lei")

expense_label=Label(app, text="Expense", font=font_large, background="goldenrod",).grid(column=0, row=0, padx=20, pady=15)

transp_label=Label(app, text="Transport", font=font_normal, background="goldenrod").grid(row=0, column=1, padx=35, pady=15)
cloth_label=Label(app, text="Clothes", font=font_normal, background="goldenrod").grid(row=0, column=2, padx=35, pady=15)
food_label=Label(app, text="Food", font=font_normal, background="goldenrod").grid(row=0, column=3, padx=35, pady=15)
other_label=Label(app, text="Other", font=font_normal, background="goldenrod").grid(row=0, column=4, padx=35, pady=15)

transp_entry=Entry(app, bd=10,background="white", justify=RIGHT, textvariable=transp_value).grid(row=1, column=1, padx=55, pady=30)
cloth_entry=Entry(app, bd=10,background="white",justify=RIGHT, textvariable=cloth_value).grid(row=1, column=2, padx=35, pady=30)
food_entry=Entry(app, bd=10,background="white",justify=RIGHT, textvariable=food_value).grid(row=1, column=3, padx=35, pady=30)
other_entry=Entry(app, bd=10,background="white",justify=RIGHT,textvariable=other_value).grid(row=1, column=4, padx=35, pady=30)

income_label=Label(app, text="Income", font=font_large, background="goldenrod").grid(column=0, row=2, padx=20, pady=15)

salary_label=Label(app, text="Salary", font=font_normal, background="goldenrod").grid(row=2, column=1, padx=35, pady=15)
gift_label=Label(app, text="Gifts", font=font_normal, background="goldenrod").grid(row=2, column=2, padx=35, pady=15)
random_money_label=Label(app, text="RandomMoney", font=font_normal, background="goldenrod").grid(row=2, column=3, padx=35, pady=15)

salary_entry=Entry(app, bd=10,background="white", justify=RIGHT,textvariable=salary_value).grid(row=3, column=1, padx=55, pady=30)
gift_entry=Entry(app, bd=10,background="white",justify=RIGHT, textvariable=gift_value).grid(row=3, column=2, padx=35, pady=30)
random_money_entry=Entry(app, bd=10,background="white", justify=RIGHT,textvariable=random_money_value).grid(row=3, column=3, padx=35, pady=30)


bdg_label1=Label(app, textvariable=money, font=font_large, background="goldenrod").grid(column=0, row=4, padx=20, pady=15)


submit_button=Button(app, text="Submit", height=2, width=20, font=font_large, activebackground="grey", background="white", bd=5,command=lambda:[submt(),show_statistic()]).place(x=400, y=400)


app.mainloop()

