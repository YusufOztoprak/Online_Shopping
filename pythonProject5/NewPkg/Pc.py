from pythonProject5.NewPkg import Technology
import pandas as pd


class Pc(Technology.Technology):

    def calculate_discounted_price(self, discount_rate = 0.05):
        discounted_price = self.get__price() * (1 - discount_rate)
        # Minimum fiyat kontrolü
        if discounted_price < 5000:
            return 5000
        return discounted_price


    PcList = []


    def __init__(self,id, name, price, amount, warranty, ram, storage):
        super().__init__(id, name, price, amount, warranty, ram, storage)
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
            "storage": [self.get_storage()]
        })

        # Eğer dosya zaten varsa veriyi güncelleriz; yoksa yeni bir dosya oluştururuz
        try:
            # Var olan dosyayı oku ve yeni veriyle birleştir
            mevcut_veri = pd.read_excel("Pc_urunleri.xlsx")
            if yeni_veri["id"].iloc[0] in mevcut_veri["id"].values:
                return

            yeni_veri = pd.concat([mevcut_veri, yeni_veri], ignore_index=True)
        except FileNotFoundError:
            # Dosya yoksa hata alırız ve yeni dosya oluştururuz
            pass

        # Yeni veya güncellenmiş veriyi Excel'e kaydet
        yeni_veri.to_excel("Pc_urunleri.xlsx", index=False)
        print("veri başarıyla kaydedildi..")

    def get_warranty(self):
        return self.warranty

    def get_ram(self):
        return self.ram

    def get_storage(self):
        return self.storage

    def set_warranty(self, new_warranty):
        self.warranty = new_warranty

    def set_ram(self, new_ram):
        self.ram = new_ram

    def set_storage(self, new_storage):
        self.storage = new_storage

    def addPc(self, new_pc):
        self.PcList.append(new_pc)

    def printPcList(self):
        for pc in self.PcList:
            print(pc.getName(), pc.getPrice())

    def getinfo(self):
        super().getinfo()
        print(" ")
