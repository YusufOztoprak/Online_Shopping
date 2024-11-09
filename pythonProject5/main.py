from pythonProject5.NewPkg.Pc import Pc
from pythonProject5.NewPkg.Phone import Phone
from pythonProject5.NewPkg.customer import customer


def main():
    customer1 = customer("Ahmet", "ahmet@gmail.com", "Malatya", "085067055" ,[])
    phone1 = Phone("samsung", 2000, 1, 2, 16, 512, True, 50, True)
    Phone.Phones.append(phone1)

    while True:
        print("\n İşlem seçiniz :")
        print("1 : Kategori Seçiniz :")
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
                    for i, phone in enumerate(Phone.Phones,start= 1):
                        print(f"{i}.{phone.get__name()}")
                    c = int(input("Sepete ekelemek istediğiniz ürünü seçiniz :"))
                    customer1.add_product(Phone.Phones[c-1])
                if (islem2 == 2):
                    c = int(input("Sepete ekelemek istediğiniz ürünü seçiniz :"))
                    for i, pc in enumerate(Pc.PcList, start=1):
                        print(f"{i}.{pc.get__name()}")
                    c = int(input("Sepete ekelemek istediğiniz ürünü seçiniz :"))
                    customer1.add_product(Pc.PcList[c-1])
        elif islem == 2:
            customer1.show_cart()
if __name__ == "__main__":
    main()








