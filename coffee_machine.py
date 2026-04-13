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

    def add_extra_sugar(self):

        self.extra_sugar += 5
        messagebox.showinfo("Extra Sugar", "Extra sugar added")

    def place_order(self):

        if not self.order_cart:
            messagebox.showerror("Order","No items in order")
            return

        order_details = "\n".join(self.order_cart)

        confirm = messagebox.askyesno(
            "Confirm Order",
            f"Items:\n{order_details}\n\nTotal Cost: {self.total_cost} Rs"
        )

        if not confirm:
            # clear the cart if user cancels
            self.order_cart = []
            self.total_cost = 0
            self.extra_sugar = 0
            messagebox.showinfo("Order Cancelled","Previous order cleared")
            return

        if self.process_payment(self.total_cost):

            for item in self.order_cart:
                drink = self.menu[item]
                self.deduct_resources(drink["ingredients"])
                self.profit += drink["profit"]

            if self.extra_sugar > 0:
                self.resources["sugar"] -= self.extra_sugar

            self.money += self.total_cost

            messagebox.showinfo("Coffee Machine","Order Ready ❤️ Enjoy!")

        else:
            messagebox.showinfo("Order Cancelled","Order cleared due to insufficient payment")
         
        self.order_cart = []
        self.total_cost = 0
        self.extra_sugar = 0

    def admin_login(self):

        password = simpledialog.askstring("Admin","Enter admin password", show="*")

        if password == self.admin_password:
            return True
        else:
            messagebox.showerror("Access","Wrong password")
            return False
    def report(self):

        if not self.admin_login():
            return

        report_text = f"""
Milk: {self.resources['milk']} ml
Milk Foam: {self.resources['milk_foam']} ml
Coffee: {self.resources['coffee']} gm
Sugar: {self.resources['sugar']} gm

Money: {self.money} Rs
Profit: {self.profit} Rs
"""

        messagebox.showinfo("Machine Report", report_text)
   
    def refill(self):

        if not self.admin_login():
            return

        milk = simpledialog.askinteger("Refill","Add milk (ml)")
        sugar = simpledialog.askinteger("Refill","Add sugar (gm)")
        coffee = simpledialog.askinteger("Refill","Add coffee (gm)")
        foam = simpledialog.askinteger("Refill","Add milk foam (ml)")

        self.resources["milk"] += milk
        self.resources["sugar"] += sugar
        self.resources["coffee"] += coffee
        self.resources["milk_foam"] += foam

        messagebox.showinfo("Refill","Resources refilled")
        
    def off(self):

        if not self.admin_login():
            return

        root.destroy()

machine = CoffeeMachine()

root = Tk()
root.title("Coffee Machine")
root.geometry("400x550")
root.config(bg="gray")
root.option_add("*Font", "Arial 16")

title = Label(root,text="Coffee Machine",font=("Courier New",25,"bold"),
              bg="saddlebrown",fg="gold")
title.pack(pady=10)

btn1 = Button(root,text="Coffee (80Rs)",font=("fixedsys",13),relief=RAISED,bg="seagreen",width=18,
                 command=lambda: machine.add_to_order("coffee"))
btn1.place(x=123,y=80)

btn2 = Button(root,text="Latte (150Rs)",font=("fixedsys",13),relief=RAISED,bg="seagreen",width=18,
                 command=lambda: machine.add_to_order("latte"))
btn2.place(x=123,y=125)

btn3 = Button(root,text="Cappuccino (120Rs)",font=("fixedsys",13),relief=RAISED,bg="seagreen",width=18,
                 command=lambda: machine.add_to_order("cappuccino"))
btn3.place(x=123,y=170)

# extra sugar button
sugar_btn = Button(root,text="Extra Sugar",relief=RAISED,bg="tan",font=("Arial",13,"italic"),width=13,
                   command=machine.add_extra_sugar)
sugar_btn.place(x=25,y=245)

# place order button
order_btn = Button(root,text="Place Order",relief=RAISED,bg="tan",font=("Arial",13,"italic"),width=13,
                   command=machine.place_order)
order_btn.place(x=235,y=245)

admin_txt=Label(root,text="Admin Options",bg="crimson",
                font=("Courier New",12,"bold"))
admin_txt.place(x=133, y=330)

report_btn =Button(root,text="Report",relief=RAISED,bg="pink",font=("fixedsys",13),width=18,
                       command=machine.report)
report_btn.place(x=123,y=360)

refill_btn =Button(root,text="Refill",relief=RAISED,bg="pink",font=("fixedsys",13),width=18,
                       command=machine.refill)
refill_btn.place(x=123,y=405)

off_btn =Button(root,text="Turn Off",relief=RAISED,bg="pink",font=("fixedsys",13),width=18,
                    command=machine.off)
off_btn.place(x=123,y=450)

root.mainloop()
