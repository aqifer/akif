from tkinter import *
from tkinter import messagebox
import datetime

class Pizza(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("650x550")
        self.title("Welcome to AI Pizza")
        self.create_widgets()

    def create_widgets(self):
        # isim bilgisi girisi 
        name_label = Label(self, text="What is your name? ")
        name_label.grid(row=0, column=0)

        self.name_entry = Entry(self, width=40)
        self.name_entry.grid(row=0, column=1)

        # adres bilgisi girisi 
        address_label = Label(self, text="What is your adress? ")
        address_label.grid(row=1, column=0)

        self.address_entry = Entry(self, width=40)
        self.address_entry.grid(row=1, column=1)

        # telefon bilgisi girisi 
        phone_label = Label(self, text="What is your phone number? ")
        phone_label.grid(row=2, column=0)

        self.phone_entry = Entry(self, width=40)
        self.phone_entry.grid(row=2, column=1)

        # kredi kartı bilgisi girisi
        payment_label = Label(self, text="What is your card number? ")
        payment_label.grid(row=3, column=0)

        self.payment_entry = Entry(self, width=40)
        self.payment_entry.grid(row=3, column=1)

        # kart şifre bilgisi girisi
        password_label = Label(self, text="What is your card password? ")
        password_label.grid(row=4, column=0)

        self.password_entry = Entry(self, width=40)
        self.password_entry.grid(row=4, column=1)

        # pizza seçenekleri ve fiyatları 
        self.ai_pizza_list = {"Classic": 10,
                              "Margherita": 12,
                              "TurkPizza": 15,
                              "PlainPizza": 8}

        self.dataTest = []

        # pizza seçimine göre toplam fiyatı hesaplama
        def calculate_price(pizza_selection):
            total_price = 0
            for pizza in pizza_selection:
                total_price += self.ai_pizza_list[pizza]
            self.dataTest.append(f"{total_price} $")
            return total_price

        self.pizza_list = Listbox(self, selectmode=MULTIPLE, bg="black", fg="white")
        self.pizza_list.grid(row=8, column=1)

        for x in self.ai_pizza_list:
            self.pizza_list.insert(0, x)


        #def add_pizza():
            #result = []
            #for x in "self.p"

            def add_pizza():
             selected_pizzas = [self.pizza_list.get(i) for i in self.pizza_list.curselection()]
             return selected_pizzas

