class Cart:

    def __init__(self):
        self.cart = []

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
