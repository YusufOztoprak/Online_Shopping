from pythonProject5.NewPkg.Technology import Technology
from pythonProject5.NewPkg.Product import Product
import pandas as pd



class Phone(Technology):
    Phones = []

    def __init__(self, name, price, amount, warranty, ram, storage, fiveGsupport, numberofCameras, fastCharging):
        super().__init__(name, price, amount, warranty, ram, storage)
        self.fiveGsupport = fiveGsupport
        self.numberofCameras = numberofCameras
        self.fastCharging = fastCharging
        self.Phones.append(self)
        #self.excel_kaydet()

    def excel_kaydet(self):
        # Telefon nesnesini DataFrame olarak oluştur
        yeni_veri = pd.DataFrame({
            "name": [self.get__name()],
            "price": [self.get__price()],
            "amount": [self.get__amount()],
            "warranty": [self.get_warranty()],
            "ram": [self.get_ram()],
            "storage": [self.get_storage()],
            "fiveGsupport": [self.getFiveGSupport()],
            "numberOfcameras": [self.getNumberOfCameras()],
            "fastCharging": [self.getFastCharging()],
        })

        # Eğer dosya zaten varsa veriyi güncelleriz; yoksa yeni bir dosya oluştururuz
        try:
            # Var olan dosyayı oku ve yeni veriyle birleştir
            mevcut_veri = pd.read_excel("telefon_urunleri.xlsx")
            yeni_veri = pd.concat([mevcut_veri, yeni_veri], ignore_index=True)
        except FileNotFoundError:
            # Dosya yoksa hata alırız ve yeni dosya oluştururuz
            pass

        # Yeni veya güncellenmiş veriyi Excel'e kaydet
        yeni_veri.to_excel("telefon_urunleri.xlsx", index=False)

    def __repr__(self):
        return f"Telefon({self.get__name()}, {self.get__price()}, {self.get__amount()}, {self.get_warranty()}, {self.get_ram()}, {self.get_storage()},{self.getFiveGSupport()},{self.getNumberOfCameras()},{self.getFastCharging()}"

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
"""
    veri = {"name": [telefon.get__name() for telefon in Phones],
            "price": [telefon.get__price() for telefon in Phones],
            "amount": [telefon.get__amount() for telefon in Phones],
            "warranty": [telefon.get__warranty() for telefon in Phones],
            "ram": [telefon.get__ram() for telefon in Phones],
            "storage": [telefon.get__storage() for telefon in Phones],
            "fiveGsupport": [telefon.get__fiveGsupport for telefon in Phones],
            "numberOfCameras": [telefon.get__numberOfCameras() for telefon in Phones],
            "fastCharching": [telefon.get__fastCharching() for telefon in Phones],

            }
    df = pd.DataFrame(veri)

    # Excel dosyasına yazma
    df.to_excel("telefon_urunleri.xlsx", index=False)

"""
"""
      # Telefon nesnesini DataFrame olarak oluştur
        yeni_veri = pd.DataFrame({
            "name": [self.get__name()],
            "price": [self.get__price()],
            "amount": [self.get__amount()],
            "warranty": [self.get_warranty()],
            "ram": [self.get_ram()],
            "storage": [self.get_storage()],
            "fiveGsupport": [self.getFiveGSupport()],
            "numberOfcameras": [self.getNumberOfCameras()],
            "fastCharging": [self.getFastCharging()],
        })

        # Eğer dosya zaten varsa veriyi güncelleriz; yoksa yeni bir dosya oluştururuz
        try:
            # Var olan dosyayı oku ve yeni veriyle birleştir
            mevcut_veri = pd.read_excel("telefon_urunleri.xlsx")
            yeni_veri = pd.concat([mevcut_veri, yeni_veri], ignore_index=True)
        except FileNotFoundError:
            # Dosya yoksa hata alırız ve yeni dosya oluştururuz
            pass

        # Yeni veya güncellenmiş veriyi Excel'e kaydet
        yeni_veri.to_excel("telefon_urunleri.xlsx", index=False)"""

