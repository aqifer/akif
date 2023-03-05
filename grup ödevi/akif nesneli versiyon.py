from tkinter import *
from tkinter import messagebox

class PizzaApp:

    def __init__(self, window):
        self.window = window
        self.window.geometry("650x550")
        self.window.title("Welcome to AI Pizza")

        # Labels and Entries
        name_label = Label(window, text="What is your name? ")
        name_label.grid(row=0, column=0)
        self.name_entry = Entry(window, width=40)
        self.name_entry.grid(row=0, column=1)

        address_label = Label(window, text="What is your adress? ")
        address_label.grid(row=1, column=0)
        self.address_entry = Entry(window, width=40)
        self.address_entry.grid(row=1, column=1)

        phone_label = Label(window, text="What is your phone number? ")
        phone_label.grid(row=2, column=0)
        self.phone_entry = Entry(window, width=40)
        self.phone_entry.grid(row=2, column=1)

        payment_label = Label(window, text="What is your card number? ")
        payment_label.grid(row=3, column=0)
        self.payment_entry = Entry(window, width=40)
        self.payment_entry.grid(row=3, column=1)

        password_label = Label(window, text="What is your card password? ")
        password_label.grid(row=4, column=0)
        self.password_entry = Entry(window, width=40)
        self.password_entry.grid(row=4, column=1)

        # Pizza List
        ai_pizza_list = ["Classic", "Margherita", "TurkPizza", "PlainPizza"]

        self.pizza_list = Listbox(window, selectmode=MULTIPLE, bg="black", fg="white")
        self.pizza_list.grid(row=8, column=1)

        for pizza in ai_pizza_list:
            self.pizza_list.insert(END, pizza)

        self.add_lbl = Label(window, text="")
        self.add_lbl.grid(row=5, column=1)

        add_button = Button(window, text="Add Pizza", command=self.add_pizza)
        add_button.grid(row=5, column=0)

        # Checkout Button
        check_button = Button(window, text="Checkout", command=self.check)
        check_button.grid(row=6, column=0)

        # Delete Pizza Button
        del_button = Button(window, text="Delete Pizza", command=self.delete_pizza)
        del_button.grid(row=7, column=0)

        # Pizza Materials OptionMenu
        self.materials = StringVar()
        self.materials.set("Choose materials on your pizza:")
        materials = OptionMenu(window, self.materials, "Olives", "Mushrooms", "GoatCheese", "Meat", "Onions", "Corn")
        materials.grid(row=8 , column=0)

        # Exit Button
        exit_button = Button(window, text="Exit", command=self.exit)
        exit_button.grid(row=7, column=5)

    def add_pizza(self):
        selected_pizzas = [self.pizza_list.get(i) for i in self.pizza_list.curselection()]
        self.add_lbl.config(text="Your Pizza Selection : " + "\n" + "\n".join(selected_pizzas))

    def check(self):
        name = self.name_entry.get()
        address = self.address_entry.get()
        phone = self.phone_entry.get()

        if not all((name, address, phone)):
            messagebox.showerror("Error", "Please fill all the required fields.")
        else:
            new_lbl = Label("self.window, text=")