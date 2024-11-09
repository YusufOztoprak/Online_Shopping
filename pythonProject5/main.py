from NewPkg import cart
from NewPkg import Product
from NewPkg import customer
from NewPkg import Phone
from NewPkg import *
from NewPkg import Pc


def main():
    customer1 = customer.customer("Ahmet", "ahmet@gmail.com", "Malatya", "085067055")
    customer1.show_cart()

    while True:
        print("\n İşlem seçiniz :")
        print("1 : Kategori Seçiniz :" )
        print("2 : Sepete git :")
        print("3 : Çıkış :")
        islem = int(input("hangi işlemi yapmak istiyorsunuz:"))

        if (islem == 1):
            print("\n kategori seçin:")
            print("1 : teknoloji :")
            print("2 : kişisel bakım :")
            print("3- giyim:")
            islem1 = int(input("hangi işlemi yapmak istiyorsunuz:"))
            if(islem1 == 1):
                print("\n kategori seçin:")
                print("1 : telefon :")
                print("2 : Bilgisayar :")
                islem2 = int(input("hangi işlemi yapmak istiyorsunuz:"))
                if(islem2 == 1):
                    c = int(input("Sepete ekelemek istediğiniz ürünü seçiniz :"))
                    for i,phone in enumerate(Phone.Phone.Phones,start= 1):
                        print(f"{i}.{phone.get__name()}")
                    customer1.add_product(Phone.Phones[i])
                if (islem2 == 2):
                    c = int(input("Sepete ekelemek istediğiniz ürünü seçiniz :"))
                    for i, pc in enumerate(Pc.Pc.List, start=1):
                        print(f"{i}.{pc.get__name()}")
                    customer1.add_product(Pc.PcList[i])











