from pythonProject5.NewPkg import cart

import uuid

class customer:

    def __init__(self, name, email,address, phone_number , cart:cart):
        self.__name = name
        self.__email = email
        self.__address = address
        self.__phone_number = phone_number
        self.__Id = uuid.uuid4()
        self.cart = cart

    def add_product(self, product):
        self.cart.append(product)

    def remove_product(self, product):
        if product in self.cart:
            self.cart.remove(product)
        else:
            print(f"{product.get__name()} is not in the cart.")

    def total_price(self):
        total = 0
        for product in self.cart:
            total += product.price
        return total

    def clear_cart(self):
        self.cart = []

    def show_cart(self):
        if not self.cart:
            print("Your cart is empty.")
        else:
            print("Your cart contains:")
            for product in self.cart:
                print(product.get__name())

    def get__Id(self):
        return self.__Id
    def get__name(self):
        return self.__name

    def set__name(self, name):
        self.__name = name

    def get__email(self):
        return self.__email

    def set__email(self,email):
        self.__email = email

    def get__address(self):
        return self.__address

    def set__address(self, address):
        self.__address = address

    def getphone_number(self):
        return self.__phone_number

    def setphone_number(self,phone_number):
        self.__phone_number = phone_number


    def get_info(self):
        print(f"isim: {self.get__name()}\nemail: {self.get__email()}\naddress: {self.get__address()}\nmüşteri Id: {self.get__Id()}")




# nesne oluşturabiliyoruz
# customer2 = customer("mehmet", "my0308", "malatya")
#print(customer1.get__address())
#customer1.set__address("hatay")
#print(customer1.get__address())
#customer1.get_info()