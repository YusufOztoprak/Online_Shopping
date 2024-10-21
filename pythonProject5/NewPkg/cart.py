from NewPkg import Product

class Cart:
    def_init__(self): 
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)
        
    def total_price(self):
        total = 0
        for product in self.products:
            total += product._get_price() * product._get_quantity()
        return total
    
    def clear_cart():
        self.products = []
