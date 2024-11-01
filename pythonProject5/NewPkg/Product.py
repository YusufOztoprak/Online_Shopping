import uuid
class Product:

    products = []

    def __init__(self, name, price, amount):
        self.__name = name
        self.__price = price
        self.__amount = amount
        self.__Id = uuid.uuid4()

    def add_product(self, product):
        Product.products.append(product)

    def remove_product(self,product):
        Product.products.remove(product)

    def get__name(self):
        return self.__name

    def get__price(self):
        return  self.__price

    def get__amount(self):
        return self.__amount

    def get__Id(self):
        return  self.__Id

    def set__name(self,name):
        self.__name = name

    def  set__price (self,price):
        self.__price = price

    def set__amount(self, amount):
        self.__amount = amount

    def set__Id(self, Id):
        self.__Id = Id



    @classmethod
    def listeyiyazdir(self):
        for i in Product.products:
            print(i.get__name())



"""p1 = Product("akvaryum", 100,2)
Product.listeyiyazdir()"""


