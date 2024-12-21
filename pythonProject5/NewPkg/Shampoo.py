import Personal_Care
import pandas as pd
class Shampoo(Personal_Care):
    Shampoo_list = []

    def __init__(self, name, price, amount, Id,expiration_date,brand,paraben,hairType,volume):
        super().__init__(name,price,amount,expiration_date,Id,brand)
        self.paraben = paraben
        self.hairType = hairType
        self.volume = volume
        self.excel_kaydet()

    def excel_kaydet(self):

        yeni_veri = pd.DataFrame({
            "id": [self.get__id()],
            "name": [self.get__name()],
            "price": [self.get__price()],
            "amount": [self.get__amount()],
            "expiration_date": [self.get_expiration_date()],
            "brand": [self.get_brand()],
            "paraben": [self.getParaben()],
            "hairType": [self.getHairType()],
            "volume": [self.getVolume()],

        })

        # Eğer dosya zaten varsa veriyi güncelleriz; yoksa yeni bir dosya oluştururuz
        try:
            # Var olan dosyayı oku ve yeni veriyle birleştir
            mevcut_veri = pd.read_excel("sampuan_urunleri.xlsx")
            if yeni_veri["id"].iloc[0] in mevcut_veri["id"].values:
                print("bu ürün zaten mevcut")
                return

            yeni_veri = pd.concat([mevcut_veri, yeni_veri], ignore_index=True)
        except FileNotFoundError:
            # Dosya yoksa hata alırız ve yeni dosya oluştururuz
            pass

        # Yeni veya güncellenmiş veriyi Excel'e kaydet
        yeni_veri.to_excel("sampuan_urunleri.xlsx", index=False)
        print("veri başarıyla kaydedildi..")

    def isSuitableforHairType(self,hairType):
        if(hairType.lower()  == self.hairType.lower()): return "This shampoo is suitable for your hair"
        else:
            return "This shampoo is not suitable for your"
    
    def getParaben(self):
        return self.paraben
    
    def getHairType(self):
        return self.hairType
    
    def getVolume(self):
        return self.volume
    
    def setParaben(self,paraben):
        self.paraben = paraben
        
    def setHairType(self,hairType):
        self.hairType = hairType
        
    def setVolume(self,volume):
        self.volume = volume

    def addShampoo(self):
        Shampoo.Shampoo_list.append(self)

    @classmethod
    def list_shampoos(cls):
        return cls.Shampoo_list

    @classmethod
    def find_by_brand(cls, brand):
        return [shampoo for shampoo in cls.Shampoo_list if shampoo.brand.lower() == brand.lower()]
    @staticmethod
    def __str__(self):
        return (f"Shampoo(Name: {self.name}, Price: {self.price}, Amount: {self.amount}, "
                f"ID: {self.Id}, Expiration Date: {self.expiration_date}, Brand: {self.brand}, "
                f"Paraben: {self.paraben}, Hair Type: {self.hairType}, Volume: {self.volume}ml)")


