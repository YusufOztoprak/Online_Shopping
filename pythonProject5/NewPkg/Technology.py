class Technology:
    def __init__(self, warranty,ram, storage):
        self.warranty = warranty
        self.ram = ram
        self.storage = storage


    def get_warranty(self):
        return self.warranty

    def get_ram(self):
        return self.ram

    def get_storage(self):
        return self.storage

    def set_warranty(self, warranty):
        self.warranty = warranty

    def set_ram(self,ram):
        self.ram = ram

    def set_storage(self,storage):
        self.storage = storage

