from abc import ABC, abstractmethod
from colorama import Fore, Style

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
    def getinfo(self):
        print(f"{Fore.BLUE}ürün ismi:{Style.RESET_ALL}", self.get__name())
        print(f"{Fore.BLUE}ürün fiyatı:{Style.RESET_ALL}",self.get__price())
        print(f"{Fore.BLUE}ürün miktarı:{Style.RESET_ALL}",self.__amount)
        print(f"{Fore.BLUE}ürün kimliği:{Style.RESET_ALL}", self.get__id())

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
