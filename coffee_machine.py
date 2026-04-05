from tkinter import *
from tkinter import simpledialog, messagebox


class CoffeeMachine:

    def __init__(self):

        self.resources = {
            "milk": 1000,
            "sugar": 200,
            "coffee": 300,
            "milk_foam": 500
        }

        self.menu = {
            "coffee": {
                "ingredients": {"milk":100,"sugar":15,"coffee":20},
                "price":80,
                "profit":20
            },
            "latte": {
                "ingredients":{"milk":150,"sugar":20,"coffee":30},
                "price":150,
                "profit":30
            },
            "cappuccino": {
                "ingredients":{"milk":60,"milk_foam":60,"sugar":20,"coffee":30},
                "price":120,
                "profit":30
            }
        }

        self.money = 0
        self.profit = 0
        self.admin_password = "admin123"

        self.order_cart = []
        self.total_cost = 0
        self.extra_sugar = 0

    def check_resources(self, ingredients):
        for item in ingredients:
            if self.resources[item] < ingredients[item]:
                messagebox.showerror("Error", f"{item} is insufficient")
                return False
        return True

    def deduct_resources(self, ingredients):
        for item in ingredients:
            self.resources[item] -= ingredients[item]

    def process_payment(self, price):

        five = simpledialog.askinteger("Coins","5Rs coins?")
        ten = simpledialog.askinteger("Coins","10Rs coins?")
        twenty = simpledialog.askinteger("Coins","20Rs coins?")

        total = five*5 + ten*10 + twenty*20

        if total < price:
            messagebox.showerror("Payment","Insufficient money")
            return False

        if total > price:
            messagebox.showinfo("Change", f"Return change {total-price} Rs")

        return True
        
    def add_to_order(self, choice):

        drink = self.menu[choice]

        if self.check_resources(drink["ingredients"]):

            self.order_cart.append(choice)
            self.total_cost += drink["price"]

            messagebox.showinfo("Order Added", f"{choice} added to order")

