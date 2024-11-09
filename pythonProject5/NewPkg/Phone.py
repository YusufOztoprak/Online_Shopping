from pythonProject5.NewPkg.Technology import Technology


class Phone(Technology):
    Phones = []

    def __init__(self, name, price, amount, warranty, ram, storage, fiveGsupport, numberofCameras, fastCharging):
        super().__init__(name, price, amount, warranty, ram, storage)
        self.fiveGsupport = fiveGsupport
        self.numberofCameras = numberofCameras
        self.fastCharging = fastCharging

    def getFiveGSupport(self):
        return self.fiveGsupport

    def setFiveGSupport(self, FiveGSupport):
        self.fiveGsupport = FiveGSupport

    def getNumberOfCameras(self):
        return self.numberofCameras

    def setNumberOfCameras(self, numberOfCameras):
        self.numberofCameras = numberOfCameras

    def getFastCharging(self):
        return self.fastCharging

    def setFastCharging(self):
        self.fastCharging = True

    def addPhone(self, phone):
        self.Phones.append(phone)

    def ListPhones(self):
        for i in self.Phones:
            print(i.getName(), i.getPrice())
