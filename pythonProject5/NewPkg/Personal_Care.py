from pythonProject5.NewPkg.Product import Product
from abc import ABC, abstractmethod
from colorama import Fore, Style

class PersonalCare(Product):

    @abstractmethod
    def calculate_discounted_price(self):
        pass
    PersonalCare_list = []

    def __init__(self, id, name, price, amount, expiration_date, brand):
        super().__init__(id, name, price, amount,)
        self.expiration_date = expiration_date
        self.brand = brand


    def getinfo(self):
        super().getinfo()
        print(f"{Fore.BLUE}ürünün son kullanma tarihi:{Style.RESET_ALL}", self.get_expiration_date())
        print(f"{Fore.BLUE}ürünün markası:{Style.RESET_ALL}", self.get_brand())

    def get_expiration_date(self):
        return self.expiration_date

    def get_brand(self):
        return self.brand

    def set_expiration_date(self, expiration_date):
        self.expiration_date = expiration_date

    def set_brand(self, brand):
        self.brand = brand

    def add_personal_care(self, item):
        PersonalCare.PersonalCare_list.remove(item)

    def remove_personal_care(self):
        PersonalCare.PersonalCare_list.remove(self)

    def findbyName(self, name):
        for personal_care in PersonalCare.PersonalCare_list:
            if personal_care.name == name:
                return True
            return False

    def findbyBrand(self, brand):
        for personal_care in PersonalCare.PersonalCare_list:
            if personal_care.brand == brand:
                return True
            return False

    def __str__(self):
        return f"PersonalCare(Name: {self.name}, Price: {self.price}, Amount: {self.amount}, ID: {self.Id}, Expiration Date: {self.expiration_date}, Brand: {self.brand})"
