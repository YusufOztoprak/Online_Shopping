class Cart:
    def_init__(self): # type: ignore
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)
        
    def total_price(self):
        total = 0
        for product in self.products:
            total += product.price
        return total
    
    def clear_cart():
        self.products = []