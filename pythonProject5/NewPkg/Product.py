import uuid


class Product:
    products = []

    def __init__(self, name, price, amount):
        self.__name = name
        self.__price = price
        self.__amount = amount
        self.__Id = uuid.uuid4()

    def getinfo(self, product):
        print(f"ürün ismi:{product.__name}")
        print(f"ürün fiyatı:{product.__price}")
        print(f"ürün miktarı:{product.__amount}")
        print(f"ürün kimliği:{product.__Id}")

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def get__name(self):
        return self.__name

    def get__price(self):
        return self.__price

    def get__amount(self):
        return self.__amount

    def get__Id(self):
        return self.__Id

    def set__name(self, name):
        self.__name = name

    def set__price(self, price):
        self.__price = price

    def set__amount(self, amount):
        self.__amount = amount

    def set__Id(self, Id):
        self.__Id = Id

    def printList(self):
        for product in self.products:
            print(product.getinfo())
