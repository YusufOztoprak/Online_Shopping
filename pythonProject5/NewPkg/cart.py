class Cart:

    def __init__(self):
        self.cart = []
        self.total = 0


    def add_product(self, product):
        self.cart.append(product)


    def remove_product(self, product):
        self.cart.remove(product)
        self.total -= product.price



    def total_price(self):
        total = 0
        for product in self.cart:
            self.total += product.price
        return self.total


    def clear_cart(self):
        self.cart = []