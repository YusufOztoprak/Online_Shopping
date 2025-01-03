from pythonProject5.NewPkg import cart

import uuid

class customer:


    def __init__(self, name, email,address, phone_number , cart:cart):
        self.__namecus = name
        self.__email = email
        self.__address = address
        self.__phone_number = phone_number
        self.__Id = uuid.uuid4()
        self.cart = cart
        self.order_history = []


    def add_product(self, product):
        self.cart.append(product)

    def remove_product(self, sec):
        for i, product in enumerate(self.cart, start=1):
            if i == sec:
                self.cart.remove(self.cart[sec-1])
                print(sec,". ürün başarıyla silindi...")
            else:
                print(f" is not in the cart.")

    def total_price(self):
        total = 0
        for product in self.cart:
            total += product.calculate_discounted_price(0.5)
        return total

    def clear_cart(self):
        self.cart = []

    def show_cart(self):
        if not self.cart:
            print("Your cart is empty.")
        else:
            print("Your cart contains:")
            for i, urun in enumerate(self.cart, start=1):
                print(f"{i}. {urun.getinfo()}")

    def get__Id(self):
        return self.__Id
    def get__namecus(self):
        return self.__name

    def set__namecus(self, name):
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

    def view_order_history(self):
        """Sipariş geçmişini göster."""
        if not self.order_history:
            print(f"{self.__namecus} has no past orders.")
        else:
            print(f"{self.__namecus}'s Order History:")
            for i, order in enumerate(self.order_history, start=1):
                print(f"{i}. Order: {order.display_order()} - Total: ${order.total_price()}")



    from pythonProject5.NewPkg import cart

class Customer:
    def __init__(self, name, email, address, phone_number, cart: cart):
        self.__namecus = name
        self.__email = email
        self.__address = address
        self.__phone_number = phone_number
        self.__Id = uuid.uuid4()
        self.cart = cart
        self.order_history = []

    def add_product(self, product):
        self.cart.append(product)

    def remove_product(self, sec):
        if 1 <= sec <= len(self.cart.items):
            self.cart.remove(self.cart.items[sec - 1])
        else:
            print("Product not found in the cart.")

    def total_price(self):
        return self.cart.total_price()

    def clear_cart(self):
        self.cart.clear()

    def show_cart(self):
        self.cart.show_cart()

    def get__Id(self):
        return self.__Id

    def get__namecus(self):
        return self.__namecus

    def set__namecus(self, name):
        self.__namecus = name

    def get__email(self):
        return self.__email

    def set__email(self, email):
        self.__email = email

    def get__address(self):
        return self.__address

    def set__address(self, address):
        self.__address = address

    def getphone_number(self):
        return self.__phone_number

    def setphone_number(self, phone_number):
        self.__phone_number = phone_number

    def get_info(self):
        print(f"Name: {self.get__namecus()}\nEmail: {self.get__email()}\nAddress: {self.get__address()}\nCustomer Id: {self.get__Id()}")

    def add_to_order_history(self):
        if not self.cart.is_empty():
            self.order_history.append(self.cart.copy())
            self.clear_cart()
            print("Order added to history.")
        else:
            print("Cart is empty. Cannot add to order history.")

    def view_order_history(self):
        if not self.order_history:
            print(f"{self.__namecus} has no past orders.")
        else:
            print(f"{self.__namecus}'s Order History:")
            for i, order in enumerate(self.order_history, start=1):
                print(f"Order {i}:")
                for product in order:
                    print(f"  - {product.get__name()} (${product.get__price()})")

# nesne oluşturabiliyoruz
# customer2 = customer("mehmet", "my0308", "malatya")
#print(customer1.get__address())
#customer1.set__address("hatay")
#print(customer1.get__address())
#customer1.get_info()