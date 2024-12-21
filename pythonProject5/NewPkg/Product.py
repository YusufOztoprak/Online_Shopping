from abc import ABC, abstractmethod

class Product():
    products = []

    def __init__(self, id, name, price, amount):
        self.__name = name
        self.__price = price
        self.__amount = amount
        self.__id = id

    @abstractmethod
    def calculate_discounted_price(self, discount_rate):
        pass
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

    def get__id(self):
        return self.__id

    def set__name(self, name):
        self.__name = name

    def set__price(self, price):
        self.__price = price

    def set__amount(self, amount):
        self.__amount = amount

    def set__id(self, id):
        self.__id = id

    def printList(self):
        for product in self.products:
            print(product.getinfo())
