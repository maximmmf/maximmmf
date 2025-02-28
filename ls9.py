import requests
import tkinter as tk
from tkinter import messagebox


class CurrencyConverter:
    def __init__(self, base_currency="UAH"):
        self.base_currency = base_currency
        self.exchange_rate = self.get_exchange_rate()

    def get_exchange_rate(self):
        url = "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            for currency in data:
                if currency["ccy"] == "USD":
                    return float(currency["sale"])
        else:
            return None

    def convert_to_usd(self, amount):
        if self.exchange_rate:
            return round(amount / self.exchange_rate, 2)
        else:
            return "Ошибка получения курса валют"


def convert_currency():
    try:
        amount = float(entry_amount.get())
        result = converter.convert_to_usd(amount)
        label_result.config(text=f"Эквивалент в USD: {result} $")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректное число")


converter = CurrencyConverter()

root = tk.Tk()
root.title("Конвертер валют")
root.geometry("300x200")

tk.Label(root, text="Введите сумму в UAH:", font=("Arial", 12)).pack(pady=5)
entry_amount = tk.Entry(root, font=("Arial", 12))
entry_amount.pack(pady=5)

btn_convert = tk.Button(root, text="Конвертировать", command=convert_currency, font=("Arial", 12))
btn_convert.pack(pady=10)

label_result = tk.Label(root, text="Эквивалент в USD: ", font=("Arial", 12))
label_result.pack(pady=5)

root.mainloop()