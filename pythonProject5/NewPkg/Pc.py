from Technology import Technology


class Pc(Technology):
    PcList = []
    def __init__(self, name, price, amount, warranty, ram, storage):
        super().__init__(name, price, amount, warranty, ram, storage)
        self.warranty = warranty
        self.ram = ram
        self.storage = storage

    def get_warranty(self):
        return self.warranty

    def get_ram(self):
        return self.ram

    def get_storage(self):
        return self.storage

    def set_warranty(self, new_warranty):
        self.warranty = new_warranty

    def set_ram(self,new_ram):
        self.ram = new_ram

    def set_storage(self,new_storage):
        self.storage = new_storage

    def addPc(self, new_pc):
        self.PcList.append(new_pc)

    def printPcList(self):
        for pc in self.PcList:
            print(pc.getName(), pc.getPrice())



