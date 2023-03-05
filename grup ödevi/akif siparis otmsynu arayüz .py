print("hello world")
#salffev/cemalakifözateş

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QComboBox

class PizzaOrderApp(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Pizza Sipariş Uygulaması'
        self.width = 500
        self.height = 400
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(100, 100, self.width, self.height)

        self.pizza_label = QLabel("Pizza Çeşitleri")
        self.pizza_combobox = QComboBox()
        self.pizza_combobox.addItems(["Margaritalı", "Peperoni", "Supreme", "Barbekü", "Gennora"])

        self.extra_label = QLabel("Ekstra Malzemeler")
        self.extra_combobox = QComboBox()
        self.extra_combobox.addItems(["Zeytin", "Mantar", "Kaşar", "Soğan", "Mısır", "Jambon", "Sos"])

        self.drink_label = QLabel("İçecekler")
        self.drink_combobox = QComboBox()
        self.drink_combobox.addItems(["Kola", "Soğukçay", "Gazoz", "Fanta", "Kahve", "Çay", "Ayran"])

        self.add_button = QPushButton("Siparişe Ekle")
        self.add_button.clicked.connect(self.add_to_order)

        self.order_label = QLabel("Siparişler")
        self.order_list = QLabel("")
        self.total_price_label = QLabel("Toplam Fiyat")
        self.total_price_value = QLabel("0")

        vbox1 = QVBoxLayout()
        vbox1.addWidget(self.pizza_label)
        vbox1.addWidget(self.pizza_combobox)

        vbox2 = QVBoxLayout()
        vbox2.addWidget(self.extra_label)
        vbox2.addWidget(self.extra_combobox)

        vbox3 = QVBoxLayout()
        vbox3.addWidget(self.drink_label)
        vbox3.addWidget(self.drink_combobox)

        hbox = QHBoxLayout()
        hbox.addLayout(vbox1)
        hbox.addLayout(vbox2)
        hbox.addLayout(vbox3)

        vbox4 = QVBoxLayout()
        vbox4.addLayout(hbox)
        vbox4.addWidget(self.add_button)

        vbox5 = QVBoxLayout()
        vbox5.addWidget(self.order_label)
        vbox5.addWidget(self.order_list)

        vbox6 = QVBoxLayout()
        vbox6.addWidget(self.total_price_label)
        vbox6.addWidget(self.total_price_value)

        hbox2 = QHBoxLayout()
        hbox2.addLayout(vbox5)
        hbox2.addLayout(vbox6)

        vbox7 = QVBoxLayout()
        vbox7.addLayout(vbox4)
        vbox7.addLayout(hbox2)

        self.setLayout(vbox7)

        self.show()

    def add_to_order(self):
        item = ""
        if self.pizza_combobox.currentText() != "":
            item = self.pizza_combobox.currentText()
        elif self.extra_combobox.currentText() != "":
            item = self.extra_combobox.currentText()
        elif self.drink_combobox.currentText() != "":
            item = self.drink_combobox.currentText()
        self.order_list.setText(self.order_list.text() + "\n" + item)
        self.total_price_value.setText(str(int(self.total_price_value.text()) + self.get_item_price(item)))

    def get_item(self):
    selected_item = self.tree.selection()
    if not selected_item:
        messagebox.showwarning("Hata", "Lütfen bir ürün seçin.")
        return
    values = self.tree.item(selected_item, 'values')
    return values[0]
