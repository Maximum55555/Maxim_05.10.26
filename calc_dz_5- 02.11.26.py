import tkinter as tk
from tkinter import ttk
import requests

def exchange():
    b1 = cb1.get()
    b2 = cb2.get()
    t = cb3.get()

    url = "https://www.cbr-xml-daily.ru/daily_json.js"
    data = requests.get(url).json()['Valute']

    if b1 == 'RUB':
        rub_b1 = 1
    else:
        rub_b1 = data[b1]['Value'] / data[b1]['Nominal']

    if b2 == 'RUB':
        rub_b2 = 1
    else:
        rub_b2 = data[b2]['Value'] / data[b2]['Nominal']

    if t == 'RUB':
        rub_t = 1
    else:
        rub_t = data[t]['Value'] / data[t]['Nominal']

    rate1 = rub_b1 / rub_t
    rate2 = rub_b2 / rub_t

    text1 = "1 " + b1 + " = " + str(round(rate1, 4)) + " " + t
    text2 = "1 " + b2 + " = " + str(round(rate2, 4)) + " " + t

    lbl_res.config(text=text1 + "\n\n" + text2)

win = tk.Tk()
win.title("Курсы обмена валют")
win.geometry("350x450")
win.config(bg="white")

tk.Label(win, text="Базовая валюта", font=("Arial", 10, "bold"), bg="white").pack(pady=10)

cb1 = ttk.Combobox(win, values=["EUR", "USD", "RUB"])
cb1.set("EUR")
cb1.pack()

tk.Label(win, text="Евро", bg="white").pack(pady=5)

tk.Label(win, text="2я базовая валюта", font=("Arial", 10, "bold"), bg="white").pack(pady=10)

cb2 = ttk.Combobox(win, values=["EUR", "USD", "RUB"])
cb2.set("USD")
cb2.pack()

tk.Label(win, text="Доллар США", bg="white").pack(pady=5)

tk.Label(win, text="Целевая валюта", font=("Arial", 10, "bold"), bg="white").pack(pady=10)

cb3 = ttk.Combobox(win, values=["EUR", "USD", "RUB"])
cb3.set("RUB")
cb3.pack()

tk.Label(win, text="Российский рубль", bg="white").pack(pady=5)

tk.Button(win, text="Получить курс обмена", command=exchange).pack(pady=20)

lbl_res = tk.Label(win, text="", font=("Arial", 10), bg="white")
lbl_res.pack()

win.mainloop()