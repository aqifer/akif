## Kod içerisine son paylaşımdan sonra eklenenler; kredi kartı numarası isteme modülü, kredi kartı şifresi isteme modülü, arayüz renk ve konum değişimi
##      EKSİKLERİMİZ
## Yorum satırları yazılmalı,
## Image import edebilmek için kütüphane ve kod kontrol edilmeli,
## Classları kullanmadık şuan sorun yok, classlar için ne yapacağız karar verilmeli,
## Datetime kullanmıyoruz, kullanıp, tarih verisini tutmalıyız,
## Sonuçlar grafiğe dökülmeli,
## Bütün veriler .csv dosyasında saklanmalı.

## ayten- datetime eklendi, ekrana sipariş saati yazdırıldı. Açıklama yazıları eklendi.


from tkinter import *
## from PIL import ImageTk, Image ## ModuleNotFoundError: No module named 'PIL'
from tkinter import messagebox

import datetime

order_time = str(datetime.datetime.now())




pizza = Tk()
pizza.geometry ("650x550")
pizza.title("Welcome to AI Pizza")
#isim bilgisi girisi 
name_label = Label(pizza, text = "What is your name? ")
name_label.grid(row=0, column=0)

name_entry = Entry(pizza, width = 40)
name_entry.grid(row=0, column=1)

# adres bilgisi girisi 
address_label = Label(pizza, text = "What is your adress? ")
address_label.grid(row=1, column=0)

address_entry = Entry(pizza, width = 40)
address_entry.grid(row=1, column=1)

#telefon bilgisi girisi 
phone_label = Label(pizza, text = "What is your phone number? ")
phone_label.grid(row=2, column=0)

phone_entry = Entry(pizza, width = 40)
phone_entry.grid(row=2, column=1)

#kredi kartı bilgisi girisi
payment_label = Label(pizza, text = "What is your card number? ")
payment_label.grid(row=3, column=0)

payment_entry = Entry(pizza, width = 40)
payment_entry.grid(row=3, column=1)

#kart şifre bilgisi girisi
password_label = Label(pizza, text = "What is your card password? ")
password_label.grid(row=4, column=0)

password_entry = Entry(pizza, width = 40)
password_entry.grid(row=4, column=1)

# pizza seçenekleri ve fiyatları 
ai_pizza_list = {"Classic": 10,
    "Margherita": 12,
    "TurkPizza": 15,
    "PlainPizza": 8 
}
    
# pizza seçimine göre toplam fiyatı hesaplama
def calculate_price(pizza_selection):
    total_price = 0
    for pizza in pizza_selection:
        total_price += ai_pizza_list[pizza]
    return total_price
        
## ai_pizza_list = ["Classic", "Margherita", "TurkPizza", "PlainPizza"]

pizza_list = Listbox(pizza, selectmode = MULTIPLE, bg="black", fg="white")
pizza_list.grid(row=8, column=1)

for x in ai_pizza_list:
    pizza_list.insert(0, x)

def add_pizza():
    result = []
    for x in pizza_list.curselection():
        result.append(pizza_list.get(x).split(" - ")[0])
    total_price = calculate_price(result)
    add_lbl.config(text=f"Your Pizza Selection: {', '.join(result)}\nTotal Price: ${total_price}")

add_lbl = Label(pizza, text="")
add_lbl.grid(row=5, column=1)


#pizza seçimi girisi
add_button = Button(pizza, text = "Add Pizza", command = add_pizza)
add_button.grid(row = 5, column = 0)

#siparis bilgisinin ekrana yazdırılması
def check():
    text1 = name_entry.get()
    new_lbl = Label(pizza, text="Name:" + text1)
    new_lbl.grid(row=5, column=2)

    text2 = address_entry.get()
    new_lbl2 = Label(pizza, text="Address:" + text2)
    new_lbl2.grid(row=6, column=2)

    text3 = phone_entry.get()
    new_lbl3 = Label(pizza, text="Phone Number:" + text3)
    new_lbl3.grid(row=7, column=2)

    new_lbl4 = Label(pizza, text="Sipariş tarihi: " + order_time)
    new_lbl4.grid(row=8, column=2)


check_button = Button(pizza, text="Chechout", command=check)
check_button.grid(row = 6, column = 0)


#seçimlerin iptali
def deleteme():
    pizza_list.delete(0,5)


del_button = Button(pizza, text= "Delete Pizza", command = deleteme)
del_button.grid(row=7, column=0)

#sosların tanımlanası
materials = StringVar()
materials.set("Choose materials on your pizza:")
materials = OptionMenu(pizza, materials, "Olives", "Mushrooms", "GoatCheese", "Meat", "Onions", "Corn")
materials.grid(row=8 , column=0)

##pizza_pic = ImageTk.PhotoImage(Image.open("pizza.png")) 
## pic_lbl = Label(pizza, image=pizza_pic)
## pic_lbl.grid(row=1, column=7)


def exitme():
    answer = messagebox.askyesno("GoodBye", "Are You Sure to exit?")
    if answer == 1:
        pizza.destroy()
    else:
        return


#menüden çıkmak için
exit_button = Button(pizza, text="Exit", command=exitme)
exit_button.grid(row=9, column=5)

pizza.mainloop()

import csv

# header row for csv file
header = ["Date", "Time", "Name", "Surname",]


# Example simple data
data = [
["2023-03-01", "10:00:00", "Tunahan", "AI"],
["2023-03-01", "11:00:00", "Akif", "AI"],
["2023-03-01", "12:00:00", "Ayten", "AI"],
]
    # ... add more data here ...



# write data to csv file
with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(data)