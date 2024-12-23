from pythonProject5.NewPkg.Personal_Care import PersonalCare
import pandas as pd
from abc import ABC, abstractmethod
from colorama import Fore,Style

class Perfume(PersonalCare):

    @abstractmethod
    def calculate_discounted_price(self, discount_rate):
        discounted_price = self.get__price() * (1 - discount_rate)
        return discounted_price

    def __init__(self, id, name, price, amount, expiration_date, brand, volume, gender_target, alcohol_content):
        super().__init__(id, name, price, amount, expiration_date, brand)
        self.volume = volume
        self.gender_target = gender_target
        self.alcohol_content = alcohol_content
        self.excel_kaydet()

    def excel_kaydet(self):

        yeni_veri = pd.DataFrame({
            "id": [self.get__id()],
            "name": [self.get__name()],
            "price": [self.get__price()],
            "amount": [self.get__amount()],
            "expiration_date": [self.get_expiration_date()],
            "brand": [self.get_brand()],
            "volume": [self.getVolume()],
            "gender_target": [self.getGenderTarget()],
            "alcohol_content": [self.getAlcoholContent()],
        })

        # Eğer dosya zaten varsa veriyi güncelleriz; yoksa yeni bir dosya oluştururuz
        try:
            # Var olan dosyayı oku ve yeni veriyle birleştir
            mevcut_veri = pd.read_excel("Parfume_urunleri.xlsx")
            if yeni_veri["id"].iloc[0] in mevcut_veri["id"].values:
                return

            yeni_veri = pd.concat([mevcut_veri, yeni_veri], ignore_index=True)
        except FileNotFoundError:
            # Dosya yoksa hata alırız ve yeni dosya oluştururuz
            pass

        # Yeni veya güncellenmiş veriyi Excel'e kaydet
        yeni_veri.to_excel("Parfume_urunleri.xlsx", index=False)
        print("veri başarıyla kaydedildi..")

    def displayDetails(self):
        details = f"""
        Hacim: {self.volume}ml
        Hedef Cinsiyet: {self.gender_target}
        Alkol İçeriği: {self.alcohol_content}
        """
        print(details)


    def getinfo(self):
        super().getinfo()
        print(f"{Fore.BLUE}ürünün hacmi:{Style.RESET_ALL}", self.getVolume())
        print(f"{Fore.BLUE}ürünün hedef cinsiyeti:{Style.RESET_ALL}",  self.getGenderTarget())
        print(f"{Fore.BLUE}ürünün alkol içeriği:{Style.RESET_ALL}", self.getAlcoholContent())
        print(" ")

    def getVolume(self):
        return self.volume

    def setVolume(self, volume):
        self.volume = volume

    def getAlcoholContent(self):
        return self.alcohol_content

    def setAlcoholContent(self, alcohol_content):
        self.alcohol_content = alcohol_content

    def getGenderTarget(self):
        return self.gender_target

    def setGenderTarget(self, gender_target):
        self.gender_target = gender_target

