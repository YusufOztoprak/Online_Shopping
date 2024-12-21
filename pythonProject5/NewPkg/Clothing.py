import Product
from abc import ABC, abstractmethod

class Clothing(Product,ABC):

    @abstractmethod
    def calculate_discounted_price(self, discount_rate):
        discounted_price = self.get_price() * (1 - discount_rate)
        # Minimum fiyat kontrolü
        if discounted_price < 500:
            return 500
        return discounted_price



    Clothing_List = []
    def __init__(self, name, price,amount,Id,size,cloth,color):
        super().__init__(name,price,amount,Id)
        self.size = size
        self.cloth = cloth
        self.color = color


    def get_cloth(self):
        return self.cloth

    def set_cloth(self,cloth):
        self.cloth = cloth

    def get_size(self):
        return self.size

    def set_size(self, size):
        if size in ["S", "M", "L", "XL"]:  # Example of size validation
            self.size = size
        else:
            raise ValueError("Invalid size. Choose from S, M, L, XL.")

    def set_price(self, price):
        if price > 0:
            self.price = price
        else:
            raise ValueError("Price must be a positive value.")

    def get_price(self):
        return self.price

    def filter_by_size(self, size):
        return [clothing for clothing in self.Clothing_List if clothing.size == size]

    def add_Clothing(self,clothing):
        self.Clothing_List.append(clothing)


    def print_Clothing(self):
        for clothing in self.Clothing_List:
            print(clothing.get_name())


