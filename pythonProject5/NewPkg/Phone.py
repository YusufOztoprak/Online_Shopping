from pythonProject5.NewPkg.Technology import Technology
from pythonProject5.NewPkg.Product import Product
import pandas as pd
from abc import ABC, abstractmethod


class Phone(Technology,ABC):

    @abstractmethod
    def calculate_discounted_price(self, discount_rate):
        discounted_price = self.get__price() * (1 - discount_rate)
        # Minimum fiyat kontrolü
        if discounted_price < 3000:
            return 3000
        return discounted_price

    def __init__(self, id, name, price, amount, warranty, ram, storage, fiveGsupport, numberofCameras, fastCharging):
        super().__init__(id, name, price, amount, warranty, ram, storage)
        self.fiveGsupport = fiveGsupport
        self.numberofCameras = numberofCameras
        self.fastCharging = fastCharging
        self.excel_kaydet()

    def excel_kaydet(self):
        # Telefon nesnesini DataFrame olarak oluştur
        yeni_veri = pd.DataFrame({
            "id": [self.get__id()],
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
            if yeni_veri["id"].iloc[0] in mevcut_veri["id"].values:
                print("bu ürün zaten mevcut")
                return

            yeni_veri = pd.concat([mevcut_veri, yeni_veri], ignore_index=True)
        except FileNotFoundError:
            # Dosya yoksa hata alırız ve yeni dosya oluştururuz
            pass

        # Yeni veya güncellenmiş veriyi Excel'e kaydet
        yeni_veri.to_excel("telefon_urunleri.xlsx", index=False)
        print("veri başarıyla kaydedildi..")

    """def __repr__(self):
        return f"Telefon({self.get__name()}, {self.get__price()}, {self.get__amount()}, {self.get_warranty()}, {self.get_ram()}, {self.get_storage()},{self.getFiveGSupport()},{self.getNumberOfCameras()},{self.getFastCharging()}"""


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
