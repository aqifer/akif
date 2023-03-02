print("hello world")

#salffev/akif

from tkinter import *
from tkinter import messagebox

# pizza seçenekleri ve fiyatları ile anlam
pizza_options = {
    "Classic": 10,
    "Margherita": 12,
    "TurkPizza": 15,
    "PlainPizza": 8
}

# pizza seçimine göre toplam fiyatı hesaplama
def calculate_price(pizza_selection):
    total_price = 0
    for pizza in pizza_selection:
        total_price += pizza_options[pizza]
    return total_price

# ana pencere
pizza = Tk()
pizza.geometry("650x550")
pizza.title("Welcome to AI Pizza")

# müşteri bilgi etiketleri ve girişleri
name_label = Label(pizza, text="What is your name? ")
name_label.grid(row=0, column=0)
name_entry = Entry(pizza, width=40)
name_entry.grid(row=0, column=1)

address_label = Label(pizza, text="What is your address? ")
address_label.grid(row=1, column=0)
address_entry = Entry(pizza, width=40)
address_entry.grid(row=1, column=1)

phone_label = Label(pizza, text="What is your phone number? ")
phone_label.grid(row=2, column=0)
phone_entry = Entry(pizza, width=40)
phone_entry.grid(row=2, column=1)

# pizza listbox
ai_pizza_list = ["Classic", "Margherita", "TurkPizza", "PlainPizza"]
pizza_list = Listbox(pizza, selectmode=MULTIPLE, bg="white", fg="red")
pizza_list.grid(row=4, column=1)
for x in ai_pizza_list:
    pizza_list.insert(0, f"{x} - ${pizza_options[x]}")

# pizza seçimi etiketleri ve düğmeleri
add_lbl = Label(pizza, text="")
add_lbl.grid(row=5, column=1)

def add_pizza():
    result = []
    for x in pizza_list.curselection():
        result.append(pizza_list.get(x).split(" - ")[0])
    total_price = calculate_price(result)
    add_lbl.config(text=f"Your Pizza Selection: {', '.join(result)}\nTotal Price: ${total_price}")

add_button = Button(pizza, text="Add Pizza", command=add_pizza)
add_button.grid(row=5, column=0)

del_button = Button(pizza, text="Delete Pizza", command=lambda: pizza_list.delete(0, END))
del_button.grid(row=7, column=0)

#pizza sosları seçenek menüsü
materials = StringVar()
materials.set("Choose materials on your pizza:")
materials = OptionMenu(pizza, materials, "Olives", "Mushrooms", "GoatCheese", "Meat", "Onions", "Corn")
materials.grid(row=8 , column=0)

# müşteri bilgileri kontrol
def check():
    new_lbl = Label(pizza, text="Name: " + name_entry.get())
    new_lbl.grid(row=5, column=2)
    new_lbl2 = Label(pizza, text="Address: " + address_entry.get())
    new_lbl2.grid(row=6, column=2)
    new_lbl3 = Label(pizza, text="Phone Number: " + phone_entry.get())
    new_lbl3.grid(row=7, column=2)

check_button = Button(pizza, text="Check", command=check)
check_button.grid(row=6, column=0)

# exit button
def exitme():
    answer = messagebox.askyesno("GoodBye", "Are You Sure to exit?")
    if answer:
        pizza
