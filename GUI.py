import tkinter as tk
import requests
from tkinter import *
import tkinter.messagebox 
root = tk.Tk()
 
root.title("Конвертор валют: DMC")
 
Tops = Frame(root, bg = '#e6e5e5', pady=2, width=1850, height=100, relief="ridge")
Tops.grid(row=0, column=0)
 
headlabel = tk.Label(Tops, font=('lato black', 19, 'bold'), text='Конвертор валют: Devil May Cry',
                    bg='#e6e5e5', fg='black')
headlabel.grid(row=1, column=0, sticky=W)
 
variable1 = tk.StringVar(root)
variable2 = tk.StringVar(root)
 
variable1.set("Валюта 1")
variable2.set("Валюта 2")
 
def RealTimeCurrencyConversion():
    Amount2_field.delete(0, tk.END)

    from_currency = variable1.get()
    to_currency = variable2.get()

    data: float = convert_currency(float(Amount1_field.get()), from_currency, to_currency)
 

    Amount2_field.insert(0, string=str(data))
 
def clear_all():
    Amount1_field.delete(0, tk.END)
    Amount2_field.delete(0, tk.END)
 
 
CurrenyCode_list = ["INR", "USD", "CAD", "CNY", "DKK", "EUR", "KZT", "RUB"]
 
root.configure(background='#e6e5e5')
root.geometry("450x450")
 
Label_1 = Label(root, font=('lato black', 27, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
Label_1.grid(row=1, column=0, sticky=W)
 
label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t    Сумма:  ", bg="#e6e5e5", fg="black", justify="center")
label1.grid(row=2, column=0, sticky=W, )
 
label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t    Из:  ", bg="#e6e5e5", fg="black")
label1.grid(row=3, column=0, sticky=W)
 
label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t    В:  ", bg="#e6e5e5", fg="black")
label1.grid(row=4, column=0, sticky=W)
 
label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t    Итог:  ", bg="#e6e5e5", fg="black")
label1.grid(row=8, column=0, sticky=W)
 
Label_1 = Label(root, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
Label_1.grid(row=5, column=0, sticky=W)
 
Label_1 = Label(root, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
Label_1.grid(row=7, column=0, sticky=W)
 
FromCurrency_option = tk.OptionMenu(root, variable1, *CurrenyCode_list)
ToCurrency_option = tk.OptionMenu(root, variable2, *CurrenyCode_list)
 
FromCurrency_option.grid(row=3, column=0, ipadx=45, sticky=E)
ToCurrency_option.grid(row=4, column=0, ipadx=45, sticky=E)
 
Amount1_field = tk.Entry(root)
Amount1_field.grid(row=2, column=0, ipadx=28, sticky=E)
 
Amount2_field = tk.Entry(root)
Amount2_field.grid(row=8, column=0, ipadx=31, sticky=E)
 
Label_9 = Button(root, font=('arial', 15, 'bold'), text="   Конвертировать  ", padx=2, pady=2, bg="lightblue", fg="white",
                 command=RealTimeCurrencyConversion)
Label_9.grid(row=6, column=0)
 
Label_1 = Label(root, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
Label_1.grid(row=9, column=0, sticky=W)
 
Label_9 = Button(root, font=('arial', 15, 'bold'), text="   Очистить  ", padx=2, pady=2, bg="lightblue", fg="white",
                 command=clear_all)
Label_9.grid(row=10, column=0)
 
 
def get_exchange_rate(base_currency, target_currency):
    url = f"https://open.er-api.com/v6/latest/{base_currency}"
    response = requests.get(url)
    
    if response.status_code != 200:
        raise Exception("Error fetching data from the API")
    
    data = response.json()
    rates = data.get("rates")
    
    if target_currency not in rates:
        raise Exception(f"Currency {target_currency} not found.")
    
    return rates[target_currency]

def convert_currency(amount, base_currency, target_currency):
    rate = get_exchange_rate(base_currency, target_currency)
    converted_amount = amount * rate
    return converted_amount