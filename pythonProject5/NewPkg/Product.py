
class Product:

    def __init__(self,name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def _get_name(self):
        return self._name

    def _get_price(self):
        return self._price

    def _get_quantity(self):
        return self._quantity

    def displayproduct(self):
        print(f"ürün adı: {self.name}\nürün fiyatı: {self.price}\nquantity:{self.quantity}")




urun =Product("samsung", 2000, 2)

Product.displayproduct(urun)