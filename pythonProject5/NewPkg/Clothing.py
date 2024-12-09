import Product
import pandas as pd

class Clothing(Product):
    Clothing_List = []
    def __init__(self, name, price,amount,Id,size,cloth,color):
        super().__init__(name,price,amount,Id)
        self.size = size
        self.cloth = cloth
        self.color = color
        self.excel_kaydet()

    def excel_kaydet(self):

        yeni_veri = pd.DataFrame({
            "id": [self.get__id()],
            "name": [self.get__name()],
            "price": [self.get__price()],
            "amount": [self.get__amount()],
            "size": [self.get_size()],
            "brand": [self.get_cloth()],
            "paraben": [self.get_clor()],


        })

        # Eğer dosya zaten varsa veriyi güncelleriz; yoksa yeni bir dosya oluştururuz
        try:
            # Var olan dosyayı oku ve yeni veriyle birleştir
            mevcut_veri = pd.read_excel("giyim_urunleri.xlsx")
            if yeni_veri["id"].iloc[0] in mevcut_veri["id"].values:
                print("bu ürün zaten mevcut")
                return

            yeni_veri = pd.concat([mevcut_veri, yeni_veri], ignore_index=True)
        except FileNotFoundError:
            # Dosya yoksa hata alırız ve yeni dosya oluştururuz
            pass

        # Yeni veya güncellenmiş veriyi Excel'e kaydet
        yeni_veri.to_excel("giyim_urunleri.xlsx", index=False)
        print("veri başarıyla kaydedildi..")

    def get_cloth(self):
        return self.cloth

    def set_cloth(self,cloth):
        self.cloth = cloth

    def get_size(self):
        return self.size

    def set_size(self, size):
        if size in ["S", "M", "L", "XL"]:  # Example of size validation
            self.size = size
        else:
            raise ValueError("Invalid size. Choose from S, M, L, XL.")

    def set_price(self, price):
        if price > 0:
            self.price = price
        else:
            raise ValueError("Price must be a positive value.")

    def get_price(self):
        return self.price

    def get_clor(self):
        return self.color


    def filter_by_size(self, size):
        return [clothing for clothing in self.Clothing_List if clothing.size == size]

    def add_Clothing(self,clothing):
        self.Clothing_List.append(clothing)


    def print_Clothing(self):
        for clothing in self.Clothing_List:
            print(clothing.get_name())


