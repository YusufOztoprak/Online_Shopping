from Technology import Technology

class Pc(Technology):
    def __init__(self, name, price, amount, warranty, ram, storage):
        super().__init__(name, price, amount, warranty, ram, storage)