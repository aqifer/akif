from tkinter import *
from tkinter import messagebox
import datetime

class Pizza:
    def __init__(self, window):
        self.window = window
        self.window.geometry ("650x550")
        self.window.title("Welcome to AI Pizza")
        self.order_time = str(datetime.datetime.now())

        # GUI öğelerinin tanımlanması
        self.name_label = Label(self.window, text="What is your name? ")
        self.name_label.grid(row=0, column=0)
        self.name_entry = Entry(self.window, width=40)
        self.name_entry.grid(row=0, column=1)

        self.address_label = Label(self.window, text="What is your address? ")
        self.address_label.grid(row=1, column=0)
        self.address_entry = Entry(self.window, width=40)
        self.address_entry.grid(row=1, column=1)

        self.phone_label = Label(self.window, text="What is your phone number? ")
        self.phone_label.grid(row=2, column=0)
        self.phone_entry = Entry(self.window, width=40)
        self.phone_entry.grid(row=2, column=1)

        self.payment_label = Label(self.window, text="What is your card number? ")
        self.payment_label.grid(row=3, column=0)
        self.payment_entry = Entry(self.window, width=40)
        self.payment_entry.grid(row=3, column=1)

        self.password_label = Label(self.window, text="What is your card password? ")
        self.password_label.grid(row=4, column=0)
        self.password_entry = Entry(self.window, width=40)
        self.password_entry.grid(row=4, column=1)

        self.ai_pizza_list = {
            "Classic": 10,
            "Margherita": 12,
            "TurkPizza": 15,
            "PlainPizza": 8
        }

        self.pizza_list = Listbox(self.window, selectmode=MULTIPLE, bg="black", fg="white")
        self.pizza_list.grid(row=8, column=1)

        for x in self.ai_pizza_list:
            self.pizza_list.insert(0, x)

        self.add_button = Button(self.window, text="Add Pizza", command=self.add_pizza)
        self.add_button.grid(row=5, column=0)
        self.add_lbl = Label(self.window, text="")
        self.add_lbl.grid(row=5, column=1)

        self.check_button = Button(self.window, text="Checkout", command=self.checkout)
        self.check_button.grid(row=6, column=0)

        self.del_button = Button(self.window, text="Delete Pizza", command=self.delete_pizza)
        self.del_button.grid(row=7, column=0)

        self.materials = StringVar()
        self.materials.set("Choose materials on your pizza:")
        self.materials = OptionMenu(self.window, self.materials, "Olives", "Mushrooms", "GoatCheese", "Meat", "Onions", "Corn")
        self.materials.grid(row=9, column=1)

    def calculate_price(self, pizza_selection):
        """
        pizza seçimine göre toplam fiyatı hesaplayan metod.
        """
        total_price = 0
        for pizza in pizza_selection:
            total_price += self.ai_p