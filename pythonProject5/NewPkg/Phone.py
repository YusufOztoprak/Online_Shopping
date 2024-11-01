from Technology import Technology

class Phone(Technology):
    def __init__(self,  name, price, amount, warranty, ram, storage, fiveGsupport, numberofCameras, fastCharging):
        super().__init__(name, price, amount, warranty, ram, storage)
        self.fiveGsupport = fiveGsupport
        self.numberofCameras = numberofCameras
        self.fastCharging = fastCharging
