from pythonProject5.NewPkg.Order import Order
from pythonProject5.NewPkg.Parfume import Perfume
from pythonProject5.NewPkg.Phone import Phone
from pythonProject5.NewPkg.Pc import Pc
from pythonProject5.NewPkg.Shampoo import Shampoo
from pythonProject5.NewPkg.customer import customer
from pythonProject5.NewPkg.cart import Cart
from pythonProject5.NewPkg.SignİN import add_user
from pythonProject5.NewPkg.Login import cheek_paswword
from pythonProject5.NewPkg.managment import cheek

import pandas as pd
from colorama import Fore, Style

def get_integer_input(prompt):
    """Kullanıcıdan tam sayı almak için güvenli giriş."""
    while True:
        try:
            user_input = input(f"{Fore.BLUE}{prompt}{Style.RESET_ALL}")  # Mavi renkli giriş
            return int(user_input)
        except ValueError:
            print(f"{Fore.RED}Hatalı giriş! Lütfen bir sayı giriniz.{Style.RESET_ALL}")  # Kırmızı renkli hata mesajı


def get_choice_input(prompt, valid_choices):
    """Kullanıcıdan belirli bir seçim almak için güvenli giriş."""
    while True:
        choice = input(f"{Fore.BLUE}{prompt}{Style.RESET_ALL}").strip()  # Kullanıcıdan giriş mavi renk
        if choice in valid_choices:
            return choice
        else:
            print(f"{Fore.RED}Hatalı giriş! Lütfen şu seçeneklerden birini seçiniz: {Fore.YELLOW}{', '.join(valid_choices)}{Style.RESET_ALL}")
            # Hata mesajı kırmızı, seçenekler sarı

from colorama import Fore, Style

def kategori_sec():
    print(f"{Fore.YELLOW}KATEGORİLER{Style.RESET_ALL}")  # Sarı renk
    while True:
        print(f"\n{Fore.CYAN}Kategori Seçiniz:{Style.RESET_ALL}")  # Açık mavi renk
        print(f"{Fore.GREEN}1 : Teknoloji{Style.RESET_ALL}")  # Yeşil renk
        print(f"{Fore.GREEN}2 : Kişisel Bakım{Style.RESET_ALL}")
        print(f"{Fore.GREEN}3 : Giyim{Style.RESET_ALL}")
        print(f"{Fore.GREEN}4 : Çıkış{Style.RESET_ALL}")

        kategori = get_integer_input(f"{Fore.BLUE}Seçiminiz (1-3): {Style.RESET_ALL}")  # Mavi renk
        if kategori in [1, 2, 3, 4]:
            return kategori
        else:
            print(f"{Fore.RED}Geçersiz kategori! Lütfen 1, 2, 3 veya 4 seçiniz.{Style.RESET_ALL}")  # Kırmızı renk



def yonetici_girisi():
    print(f"{Fore.CYAN}***************************************************{Style.RESET_ALL}")
    print(f"{Fore.CYAN}           Yönetici giriş işlemleri.               {Style.RESET_ALL}")
    print(f"{Fore.CYAN}***************************************************{Style.RESET_ALL}")

    username_input = input(f"{Fore.BLUE}Kullanıcı Adı: {Style.RESET_ALL}")
    password_input = input(f"{Fore.BLUE}Şifre: {Style.RESET_ALL}")
    if cheek(username_input, password_input):
        print(f"{Fore.GREEN}Yönetici girişi başarılı!{Style.RESET_ALL}")
        while True:
            while True:
                kategori = kategori_sec()
                if kategori == 1:  # Teknoloji
                    print(f"{Fore.YELLOW}\nAlt Kategoriler:{Style.RESET_ALL}")
                    print(f"{Fore.YELLOW}1 : Telefon{Style.RESET_ALL}")
                    print(f"{Fore.YELLOW}2 : Bilgisayar{Style.RESET_ALL}")
                    print(f"{Fore.YELLOW}3 : geri{Style.RESET_ALL}")

                    secim = get_integer_input(f"{Fore.BLUE}Hangi alt kategoriye ürün eklemek istiyorsunuz (1-3): {Style.RESET_ALL}")
                    if secim == 1:
                        try:
                            id = input(f"{Fore.BLUE}Ürün ID: {Style.RESET_ALL}")
                            name = input(f"{Fore.BLUE}Telefon Adı: {Style.RESET_ALL}")
                            price = get_integer_input(f"{Fore.BLUE}Fiyat: {Style.RESET_ALL}")
                            amount = get_integer_input(f"{Fore.BLUE}Miktar: {Style.RESET_ALL}")
                            warranty = get_integer_input(f"{Fore.BLUE}Garanti Süresi: {Style.RESET_ALL}")
                            ram = get_integer_input(f"{Fore.BLUE}RAM: {Style.RESET_ALL}")
                            storage = get_integer_input(f"{Fore.BLUE}Depolama: {Style.RESET_ALL}")
                            fiveGsupport = get_choice_input(f"{Fore.BLUE}5G Desteği Var mı? (E/H): {Style.RESET_ALL}", ["e", "h"])
                            numberofCameras = get_integer_input(f"{Fore.BLUE}Kamera Megapiksel: {Style.RESET_ALL}")
                            fastCharging = get_choice_input(f"{Fore.BLUE}Hızlı Şarj Desteği Var mı? (E/H): {Style.RESET_ALL}", ["e", "h"])

                            new_phone = Phone(
                                id, name, price, amount, warranty, ram, storage,
                                fiveGsupport, numberofCameras, fastCharging
                            )
                            print(f"{Fore.GREEN}{new_phone.get__name()} başarıyla eklendi!{Style.RESET_ALL}")
                        except Exception as e:
                            print(f"{Fore.RED}Hata: {e}{Style.RESET_ALL}")

                    elif secim == 2:
                        try:
                            id = input(f"{Fore.BLUE}Ürün ID: {Style.RESET_ALL}")
                            name = input(f"{Fore.BLUE}Bilgisayar Adı: {Style.RESET_ALL}")
                            price = get_integer_input(f"{Fore.BLUE}Fiyat: {Style.RESET_ALL}")
                            amount = get_integer_input(f"{Fore.BLUE}Miktar: {Style.RESET_ALL}")
                            warranty = get_integer_input(f"{Fore.BLUE}Garanti Süresi: {Style.RESET_ALL}")
                            ram = get_integer_input(f"{Fore.BLUE}RAM: {Style.RESET_ALL}")
                            storage = get_integer_input(f"{Fore.BLUE}Depolama: {Style.RESET_ALL}")

                            new_pc = Pc(
                                id, name, price, amount, warranty, ram, storage
                            )
                            print(f"{Fore.GREEN}{new_pc.get__name()} başarıyla eklendi!{Style.RESET_ALL}")
                        except Exception as e:
                            print(f"{Fore.RED}Hata: {e}{Style.RESET_ALL}")
                    elif secim == 3:
                        break
                    else:
                        print(f"{Fore.RED}Geçersiz seçim!{Style.RESET_ALL}")
                elif kategori == 2:  # Kişisel Bakım
                    print(f"{Fore.YELLOW}\nAlt Kategoriler:{Style.RESET_ALL}")
                    print(f"{Fore.YELLOW}1 : Parfüm{Style.RESET_ALL}")
                    print(f"{Fore.YELLOW}2 : Şampuan{Style.RESET_ALL}")
                    print(f"{Fore.YELLOW}3 : geri{Style.RESET_ALL}")
                    secim = get_integer_input(f"{Fore.BLUE}Hangi alt kategoriye ürün eklemek istiyorsunuz (1): {Style.RESET_ALL}")
                    if secim == 1:
                        try:
                            id = input(f"{Fore.BLUE}Ürün ID: {Style.RESET_ALL}")
                            name = input(f"{Fore.BLUE}Ürün Adı: {Style.RESET_ALL}")
                            price = get_integer_input(f"{Fore.BLUE}Fiyat: {Style.RESET_ALL}")
                            amount = get_integer_input(f"{Fore.BLUE}Miktar: {Style.RESET_ALL}")
                            expiration_date = get_integer_input(f"{Fore.BLUE}Son Kullanma Tarihi: {Style.RESET_ALL}")
                            brand = input(f"{Fore.BLUE}Marka: {Style.RESET_ALL}")
                            volume = get_integer_input(f"{Fore.BLUE}Ürün Hacmi: {Style.RESET_ALL}")
                            gender_target = get_choice_input(f"{Fore.BLUE}Cinsiyet Hedefi (E/K): {Style.RESET_ALL}", ["e", "k"])
                            alcohol_content = get_choice_input(f"{Fore.BLUE}Alkol Durumu (İçerir/İçermez): {Style.RESET_ALL}", ["içerir", "içermez"])

                            new_perfume = Perfume(
                                id, name, price, amount, expiration_date, brand, volume, gender_target, alcohol_content
                            )
                            print(f"{Fore.GREEN}{new_perfume.get__name()} başarıyla eklendi!{Style.RESET_ALL}")
                        except Exception as e:
                            print(f"{Fore.RED}Hata: {e}{Style.RESET_ALL}")
                    elif secim == 2:
                        try:
                            id = input(f"{Fore.BLUE}Ürün ID: {Style.RESET_ALL}")
                            name = input(f"{Fore.BLUE}Ürün Adı: {Style.RESET_ALL}")
                            price = get_integer_input(f"{Fore.BLUE}Fiyat: {Style.RESET_ALL}")
                            amount = get_integer_input(f"{Fore.BLUE}Miktar: {Style.RESET_ALL}")
                            expiration_date = get_integer_input(f"{Fore.BLUE}Son Kullanma Tarihi: {Style.RESET_ALL}")
                            brand = input(f"{Fore.BLUE}Marka: {Style.RESET_ALL}")
                            paraben = get_choice_input(f"{Fore.BLUE}Koruyucu İçeriyor mu? (E/H): {Style.RESET_ALL}", ["e", "h"])
                            hairType = input(f"{Fore.BLUE}Saç Tipi: {Style.RESET_ALL}")
                            volume = get_integer_input(f"{Fore.BLUE}Ürün Hacmi: {Style.RESET_ALL}")

                            new_shampoo = Shampoo(
                                id, name, price, amount, expiration_date, brand, paraben, hairType, volume
                            )
                            print(f"{Fore.GREEN}{new_shampoo.get__name()} başarıyla eklendi!{Style.RESET_ALL}")
                        except Exception as e:
                            print(f"{Fore.RED}Hata: {e}{Style.RESET_ALL}")
                    elif secim == 3:
                        break
                    else:
                        print(f"{Fore.RED}Geçersiz seçim!{Style.RESET_ALL}")
                elif kategori == 3:
                    pass
                else:
                    break



    else:
        print(f"{Fore.RED}Yönetici girişi başarısız! Tekrar deneyiniz.{Style.RESET_ALL}")


def kullanici_girisi():
    print(Fore.CYAN + "***************************************************" + Style.RESET_ALL)
    print(Fore.CYAN + "             Kullanıcı giriş işlemleri.             " + Style.RESET_ALL)
    print(Fore.CYAN + "***************************************************" + Style.RESET_ALL)

    while True:
        print(" ")
        secim = get_choice_input(Fore.YELLOW + "Kayıtlı kullanıcı mısınız? (E/H): " + Style.RESET_ALL, ["E", "H"])
        print(" ")
        if secim == "H":
            new_username = input(Fore.CYAN + "Yeni Kullanıcı Adı: " + Style.RESET_ALL)
            new_password = input(Fore.CYAN + "Yeni Şifre: " + Style.RESET_ALL)
            add_user(new_username, new_password)
            print(Fore.GREEN + "Kullanıcı başarıyla eklendi!" + Style.RESET_ALL)
            break
        elif secim == "E":
            username_input = input(Fore.CYAN + "Kullanıcı Adı: " + Style.RESET_ALL)
            password_input = input(Fore.CYAN + "Şifre: " + Style.RESET_ALL)

            if cheek_paswword(username_input, password_input):
                print(Fore.GREEN + "Kullanıcı girişi başarılı!" + Style.RESET_ALL)
                customer1 = customer("Ahmet", "ahmet@gmail.com", "Malatya", "085067055", [])

                while True:
                    print(Fore.YELLOW + "\nİşlem Seçiniz:" + Style.RESET_ALL)
                    print(Fore.CYAN + "1 : Kategori Seçiniz" + Style.RESET_ALL)
                    print(Fore.CYAN + "2 : Sepete Git" + Style.RESET_ALL)
                    print(Fore.CYAN + "3 : sipariş geçmişini göster" + Style.RESET_ALL)
                    print(Fore.CYAN + "4 : Çıkış" + Style.RESET_ALL)
                    islem = get_integer_input(Fore.YELLOW + "Seçiminiz: " + Style.RESET_ALL)

                    if islem == 1:
                        print(" ")
                        kategori = kategori_sec()
                        if kategori == 1:  # Teknoloji
                            while True:
                                print(" ")
                                print(Fore.YELLOW + "Alt Kategoriler:" + Style.RESET_ALL)
                                print(Fore.CYAN + "1 - Telefon" + Style.RESET_ALL)
                                print(Fore.CYAN + "2 - Bilgisayar" + Style.RESET_ALL)
                                print(Fore.CYAN + "3 - Geri" + Style.RESET_ALL)
                                alt_kategori = get_integer_input(Fore.YELLOW + "Seçiminiz: " + Style.RESET_ALL)
                                print(" ")
                                if alt_kategori == 1:  # Telefon
                                    Phones = []
                                    try:
                                        df = pd.read_excel("telefon_urunleri.xlsx")
                                        for _, row in df.iterrows():
                                            telefon = Phone(row["id"], row["name"], row["price"], row["amount"],
                                                            row["warranty"], row["ram"], row["storage"],
                                                            row["fiveGsupport"], row["numberOfcameras"],
                                                            row["fastCharging"])
                                            Phones.append(telefon)

                                        for i, phone in enumerate(Phones, start=1):
                                            print(Fore.CYAN + f"{i}. ", end="")
                                            phone.getinfo()  # Metod zaten bilgileri yazdırıyor
                                            print(Style.RESET_ALL)

                                        secim = get_integer_input(Fore.YELLOW +
                                                                  "Sepete eklemek istediğiniz ürünü seçiniz: " +
                                                                  Style.RESET_ALL)
                                        if 1 <= secim <= len(Phones):
                                            customer1.add_product(Phones[secim - 1])
                                            print(Fore.GREEN + "Ürün sepete eklendi!" + Style.RESET_ALL)
                                        else:
                                            print(Fore.RED + "Geçersiz seçim!" + Style.RESET_ALL)
                                    except FileNotFoundError:
                                        print(Fore.RED + "Ürün dosyası bulunamadı!" + Style.RESET_ALL)
                                elif alt_kategori == 2:
                                    Pclist = []
                                    try:
                                        df = pd.read_excel("Pc_urunleri.xlsx")
                                        for _, row in df.iterrows():
                                            pc = Pc(row["id"], row["name"], row["price"], row["amount"],
                                                    row["warranty"], row["ram"], row["storage"])
                                            Pclist.append(pc)

                                        for i, pc in enumerate(Phones, start=1):
                                            print(Fore.CYAN + f"{i}. ", end="")
                                            pc.getinfo()  # Metod zaten bilgileri yazdırıyor
                                            print(Style.RESET_ALL)
                                        secim = get_integer_input(Fore.YELLOW +
                                                                  "Sepete eklemek istediğiniz ürünü seçiniz: " +
                                                                  Style.RESET_ALL)
                                        if 1 <= secim <= len(Pclist):
                                            customer1.add_product(Pclist[secim - 1])
                                            print(Fore.GREEN + "Ürün sepete eklendi!" + Style.RESET_ALL)
                                        else:
                                            print(Fore.RED + "Geçersiz seçim!" + Style.RESET_ALL)
                                    except FileNotFoundError:
                                        print(Fore.RED + "Ürün dosyası bulunamadı!" + Style.RESET_ALL)
                                elif alt_kategori == 3:
                                    break

                        elif  kategori == 2:
                            while True:
                                print(" ")
                                print(Fore.YELLOW + "Alt Kategoriler:" + Style.RESET_ALL)
                                print(Fore.CYAN + "1 - parfüm" + Style.RESET_ALL)
                                print(Fore.CYAN + "2 - şampuan" + Style.RESET_ALL)
                                print(Fore.CYAN + "3 - Geri" + Style.RESET_ALL)
                                alt_kategori = get_integer_input(Fore.YELLOW + "Seçiminiz: " + Style.RESET_ALL)
                                print(" ")
                                if alt_kategori == 1:  # Telefon
                                    parfumList = []
                                    try:
                                        df = pd.read_excel("Parfume_urunleri.xlsx")
                                        for _, row in df.iterrows():
                                            parf = Perfume(row["id"], row["name"], row["price"], row["amount"], row["expiration_date"], row["brand"],
                                                           row["volume"], row["gender_target"], row["alcohol_content"])
                                            parfumList.append(parf)

                                        for i, parf in enumerate(parfumList, start=1):
                                            print(Fore.CYAN + f"{i}. ", end="")
                                            parf.getinfo()  # Metod zaten bilgileri yazdırıyor
                                            print(Style.RESET_ALL)
                                        secim = get_integer_input(Fore.YELLOW +
                                                                  "Sepete eklemek istediğiniz ürünü seçiniz: " +
                                                                  Style.RESET_ALL)
                                        if 1 <= secim <= len(parfumList):
                                            customer1.add_product(parfumList[secim - 1])
                                            print(Fore.GREEN + "Ürün sepete eklendi!" + Style.RESET_ALL)
                                        else:
                                            print(Fore.RED + "Geçersiz seçim!" + Style.RESET_ALL)
                                    except FileNotFoundError:
                                        print(Fore.RED + "Ürün dosyası bulunamadı!" + Style.RESET_ALL)
                                elif alt_kategori == 2:
                                    sahmpolist = []
                                    try:
                                        df = pd.read_excel("sampuan_urunleri.xlsx")
                                        for _, row in df.iterrows():
                                            sahmpo = Shampoo(row["id"], row["name"], row["price"], row["amount"],
                                                    row["expiration_date"], row["brand"], row["paraben"],row["hairType"], row[ "volume"])
                                            sahmpolist.append(sahmpo)

                                        for i, sahmpo in enumerate(sahmpolist, start=1):
                                            print(Fore.CYAN + f"{i}. ", end="")
                                            sahmpo.getinfo()  # Metod zaten bilgileri yazdırıyor
                                            print(Style.RESET_ALL)
                                        secim = get_integer_input(Fore.YELLOW +
                                                                  "Sepete eklemek istediğiniz ürünü seçiniz: " +
                                                                  Style.RESET_ALL)
                                        if 1 <= secim <= len(sahmpolist):
                                            customer1.add_product(sahmpolist[secim - 1])
                                            print(Fore.GREEN + "Ürün sepete eklendi!" + Style.RESET_ALL)
                                        else:
                                            print(Fore.RED + "Geçersiz seçim!" + Style.RESET_ALL)
                                    except FileNotFoundError:
                                        print(Fore.RED + "Ürün dosyası bulunamadı!" + Style.RESET_ALL)
                                elif alt_kategori == 3:
                                    break

                    elif islem == 2:
                        while True:
                            print(Fore.YELLOW + "İşlemler:" + Style.RESET_ALL)
                            print(Fore.CYAN + "1 - Sepeti Göster" + Style.RESET_ALL)
                            print(Fore.CYAN + "2 - Sepetten Ürün Sil" + Style.RESET_ALL)
                            print(Fore.CYAN + "3 - Toplam Tutarı Göster" + Style.RESET_ALL)
                            print(Fore.CYAN + "4 - Sepeti Temizle" + Style.RESET_ALL)
                            print(Fore.CYAN + "5 - Sepeti Onayla " + Style.RESET_ALL)
                            print(Fore.CYAN + "6 - Geri Dön" + Style.RESET_ALL)
                            islem = int(input(Fore.YELLOW + "Hangi işlemi yapmak istiyorsunuz: " + Style.RESET_ALL))
                            print(" ")
                            if islem == 1:
                                customer1.show_cart()
                            elif islem == 2:
                                for i, _ in  enumerate (customer1.cart, start=1):
                                    print(i, ".ürün:", _.get__name())
                                sec = int(input(Fore.YELLOW + "Silmek istediğiniz ürünün numarası: " + Style.RESET_ALL))
                                customer1.remove_product(sec)
                            elif islem == 3:
                                print(Fore.CYAN + f"Toplam Tutar: {customer1.total_price()}" + Style.RESET_ALL)
                            elif islem == 4:
                                customer1.clear_cart()
                                print(Fore.GREEN + "Sepet temizlendi!" + Style.RESET_ALL)
                            elif islem == 5:
                                if len(customer1.cart) != 0:
                                    # Step 1: Ask the user to confirm the final cart details
                                    confirmation = input(
                                        "Are you sure you want to confirm and proceed with this cart? (yes/no): ").strip().lower()

                                    if confirmation == 'yes':
                                        # Step 2: Sepetin toplam fiyatını hesaplayalım
                                        print(f"Your total is: {customer1.total_price()}.")

                                        # Step 3: Sipariş oluşturuluyor
                                        order = Order(cart=customer1.cart, customer=customer1)
                                        order_confirmation = order.complete_order()  # Sipariş onayı
                                        print(order_confirmation)
                                        customer1.clear_cart()
                                else:
                                    print("Your cart is empty. Please add items to your cart before confirming the order.")
                            elif islem == 6:
                                break
                            else:
                                print(f"{Fore.RED}geçersiz bir girdi!{Style.RESET_ALL}")
                    elif islem == 3:
                        customer1.view_order_history()
                    elif islem == 4:
                        print(Fore.CYAN + "Çıkış yapılıyor..." + Style.RESET_ALL)
                        return
                    else:
                        print(Fore.RED + "Geçersiz seçim!" + Style.RESET_ALL)
                break
            else:
                print(
                    Fore.RED + "Giriş yapılamadı. Kullanıcı adı veya şifre hatalı! Tekrar deneyiniz." + Style.RESET_ALL)

def main():
    while True:
        print(Fore.CYAN + "\n1 : Yönetici Girişi" + Style.RESET_ALL)
        print(Fore.CYAN + "2 : Kullanıcı Girişi" + Style.RESET_ALL)
        print(Fore.CYAN + "3 : Çıkış" + Style.RESET_ALL)
        print(" ")
        giris = get_integer_input(Fore.YELLOW + "Seçiniz (1-3): " + Style.RESET_ALL)
        if giris == 1:
            yonetici_girisi()
        elif giris == 2:
            kullanici_girisi()
        elif giris == 3:
            print(Fore.GREEN + "Programdan çıkılıyor..." + Style.RESET_ALL)
            return
        else:
            print(Fore.RED + "Geçersiz seçim! Lütfen 1, 2 veya 3 seçiniz." + Style.RESET_ALL)


if __name__ == "__main__":
        main()
