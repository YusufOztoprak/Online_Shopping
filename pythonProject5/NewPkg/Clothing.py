from Product import Product

class Clothing(Product):
    def __init__(self, name, price,amount,size,color,cloth):
        super().__init__(name,price,amount)
        self.size = size
        self.color = color
        self.cloth = cloth

    def get_size(self):
        return self.size

    def get_color(self):
        return self.color

    def get_cloth(self):
        return self.cloth

    def set_size(self,size):
        self.size = size

    def set_color(self,color):
        self.color = color

    def set_cloth(self,cloth):
        self.cloth = cloth

