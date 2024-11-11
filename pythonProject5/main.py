from pythonProject5.NewPkg.Pc import Pc
from pythonProject5.NewPkg.Phone import Phone
from pythonProject5.NewPkg.customer import customer
from pythonProject5.NewPkg.cart import Cart
from pythonProject5.NewPkg import Login
from  pythonProject5.NewPkg.SignİN import add_user
from pythonProject5.NewPkg.Login import cheek_paswword




def main():
    secim = input("kayıtlı kullanıcı mısınız?:")
    if(secim == "H"):
        new_username = input("Yeni kullanıcı adı:")
        new_password = input("Yeni kullanıcı şifresi:")
        add_user(new_username, new_password)
    elif(secim == "E"):
        username_input = input("kullanıcı adı:")
        password_input = input("kullanıcı şifresi:")

        dogru = cheek_paswword(username_input, password_input)

        if(dogru == True):
            customer1 = customer("Ahmet", "ahmet@gmail.com", "Malatya", "085067055", [])
            Phone1 = Phone("samsung", 2, 2, 2, 2, 1, True, 50, True)

            phone2 = Phone("apple", 2, 2, 2, 2, 2, True, 50, True)



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
                            for i, phone in enumerate(Phone.Phones, start=1):
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
                    print("işlemler:")
                    print("1-sepeti göster:")
                    print("2-sepetten ürün sil:")
                    print("3-toplam tutarı göster:")
                    print("4-sepeti temizle")
                    print("5- geri dön")
                    islem = int(input("hangi işlemi yapmak istiyorsunuz:"))
                    if(islem == 1):
                        customer1.show_cart()
                    elif(islem == 2):
                        customer1.remove_product()
                    elif(islem == 3):
                        customer1.total_price()
                    elif(islem == 4):
                        customer1.clear_cart()
                    elif(islem == 5):
                        continue
                elif islem == 3:
                    break
        else:
            print("giriş yapılamadı...")
            return



if __name__ == "__main__":
    main()








