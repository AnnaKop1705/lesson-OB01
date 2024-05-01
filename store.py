class Store():
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, item_price):
        self.items[item_name] = item_price
        print(f'Товар {item_name} успешно добавлен в ассортимент магазина {self.name}')

    def delete_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f'Товар {item_name} удален из ассортимента магазина {self.name}')
        else:
            print(f'Товара {item_name} нет в ассортименте магазина {self.name}')

    def show_price(self, item_name):
        print(self.items.get(item_name, None))

    def new_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f'Цена {item_name} в магазине {self.name} теперь {new_price}')
        else:
            print(f'Товара {item_name} нет в ассортименте магазина {self.name}')

    def show_price_list(self):
        print(f"Прайс-лист магазина {self.name}:")
        for item, price in self.items.items():
            print(f"{item}: {price} руб")

store_1 = Store('Березка', 'ул. Строителей, д. 1')
store_2 = Store('Рябинка', 'ул. Яковлева, д. 5')
store_3 = Store('Юбилейный', 'ул. Рабочая, д. 2')

store_1.add_item("Батон нарезной", 60)
store_1.add_item("Хлеб Дарницкий", 65)
store_1.add_item("Молоко", 100)

store_2.add_item("Батон нарезной", 65)
store_2.add_item("Хлеб Дарницкий", 70)
store_2.add_item("Молоко", 105)

store_3.add_item("Батон нарезной", 50)
store_3.add_item("Хлеб Дарницкий", 55)
store_3.add_item("Молоко", 90)

store_1.show_price_list()

store_1.show_price("Молоко")
store_1.new_price("Молоко", 120)
store_1.show_price("Молоко")
store_1.delete_item("Хлеб Дарницкий")
store_1.show_price_list()
store_1.show_price("Хлеб Дарницкий")