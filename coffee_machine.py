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
