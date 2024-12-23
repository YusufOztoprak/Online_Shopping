from pythonProject5.NewPkg.Product import Product
from abc import ABC,abstractmethod
from colorama import Fore, Style

class Technology(Product):


    @abstractmethod
    def calculate_discounted_price(self, discount_rate):
        pass

    listTec = []
    def __init__(self, id, name, price, amount, warranty, ram, storage):
        super().__init__(id, name, price, amount)
        self.warranty = warranty
        self.ram = ram
        self.storage = storage


    def get_warranty(self):
        return self.warranty

    def get_ram(self):
        return self.ram

    def get_storage(self):
        return self.storage

    def set_warranty(self, warranty):
        self.warranty = warranty

    def set_ram(self,ram):
        self.ram = ram

    def set_storage(self, storage):
        self.storage = storage

    def getinfo(self):
        super().getinfo()
        print(f"{Fore.BLUE}ürünün garanti süresi:{Style.RESET_ALL} ", self.get_warranty())
        print(f"{Fore.BLUE}ürünün depolama alanı:{Style.RESET_ALL} ", self.get_storage())
        print(f"{Fore.BLUE}ürünün ram kapasitesi:{Style.RESET_ALL} ", self.get_ram())









