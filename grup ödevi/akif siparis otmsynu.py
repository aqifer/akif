print("hello world")
#salffev/cemal akif özateş

class Menu:
    def __init__(self):
        self.pizzas = {
            "Margaritalı": 37,
            "Peperoni": 33,
            "Supreme": 41,
            "Barbekü": 39,
            "Gennora": 36
        }
        self.extras = {
            "Zeytin": 3,
            "Mantar": 7,
            "Kaşar": 10,
            "Soğan": 8,
            "Mısır": 5,
            "Jambon": 20,
            "Sos": 7
        }
        self.drinks = {
            "Kola": 15,
            "Soğukçay": 15,
            "Gazoz": 15,
            "Fanta": 15,
            "Kahve": 20,
            "Çay": 7,
            "Ayran": 20
        }
        self.order = []
        self.total_price = 0

    def show_pizzas(self):
        print("\nPizza Çeşitleri:")
        for pizza, price in self.pizzas.items():
            print(f"{pizza} - {price} TL")

    def show_extras(self):
        print("\nEkstra Malzemeler:")
        for extra, price in self.extras.items():
            print(f"{extra} - {price} TL")

    def show_drinks(self):
        print("\nİçecekler:")
        for drink, price in self.drinks.items():
            print(f"{drink} - {price} TL")

    def add_to_order(self, item):
        self.order.append(item)

    def calculate_total_price(self):
        for item in self.order:
            if item in self.pizzas:
                self.total_price += self.pizzas[item]
            elif item in self.extras:
                self.total_price += self.extras[item]
            elif item in self.drinks:
                self.total_price += self.drinks[item]

    def show_order(self):
        print("\nSiparişiniz:")
        for item in self.order:
            print(item)
        print(f"Toplam Fiyat: {self.total_price} TL")

menu = Menu()
while True:
    print("\nNe sipariş etmek istersiniz?\n1. Pizza Çeşitleri\n2. Ekstra Malzemeler\n3. İçecekler\n4. Siparişi Tamamla\n5. Çıkış")
    choice = input("Seçiminiz: ")
    if choice == "1":
        menu.show_pizzas()
        pizza_choice = input("Hangi pizzayı istersiniz?: ")
        menu.add_to_order(pizza_choice)
    elif choice == "2":
        menu.show_extras()
        extra_choice = input("Hangi ekstraları istersiniz?: ")
        menu.add_to_order(extra_choice)
    elif choice == "3":
        menu.show_drinks()
        drink_choice = input("Hangi içecekleri istersiniz?: ")
        menu.add_to_order(drink_choice)
    elif choice == "4":
        menu.calculate_total_price()
        menu.show_order()
        break
    elif choice == "5":
        break
    else:
        print("Geçersiz seçim, lütfen tekrar deneyin.") 

                                