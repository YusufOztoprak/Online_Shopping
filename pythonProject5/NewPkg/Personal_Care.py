from Product import Product

class PersonalCare(Product):
    def __init__(self, name, price,amount,Id,expiration_date,brand):
        super().__init__(name ,price,amount,Id)
        self.expiration_date = expiration_date
        self.brand = brand


    def get_expiration_date(self):
        return self.expiration_date

    def get_brand(self):
        return self.brand

    def set_expiration_date(self,expiration_date):
        self.expiration_date = expiration_date

    def set_brand(self,brand):
        self.brand = brand

