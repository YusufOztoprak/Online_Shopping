from pythonProject5.NewPkg.Parfume import Perfume
from pythonProject5.NewPkg.Phone import Phone
from pythonProject5.NewPkg.Pc import Pc
from pythonProject5.NewPkg.customer import customer
from pythonProject5.NewPkg.cart import Cart
from pythonProject5.NewPkg.SignİN import add_user
from pythonProject5.NewPkg.Login import cheek_paswword
from pythonProject5.NewPkg.managment import cheek

import pandas as pd
from colorama import Fore, Style, init

# Colorama'yı başlatıyoruz
init(autoreset=True)

def get_integer_input(prompt):
    """Kullanıcıdan tam sayı almak için güvenli giriş."""
    while True:
        try:
            return int(input(Fore.CYAN + prompt))
        except ValueError:
            print(Fore.RED + "Hatalı giriş! Lütfen bir sayı giriniz.")

def get_choice_input(prompt, valid_choices):
    """Kullanıcıdan belirli bir seçim almak için güvenli giriş."""
    while True:
        choice = input(Fore.YELLOW + prompt).strip()
        if choice in valid_choices:
            return choice
        else:
            print(Fore.RED + f"Hatalı giriş! Lütfen şu seçeneklerden birini seçiniz: {', '.join(valid_choices)}")

def kategori_sec():
    print(Fore.MAGENTA + "KATEGORİLER")
    while True:
        print(Fore.GREEN + "\nKategori Seçiniz:")
        print(Fore.BLUE + "1 : Teknoloji")
        print(Fore.BLUE + "2 : Kişisel Bakım")
        print(Fore.BLUE + "3 : Giyim")
        print(Fore.BLUE + "4 : Çıkış")
        kategori = get_integer_input(Fore.CYAN + "Seçiminiz (1-4): ")
        if kategori in [1, 2, 3, 4]:
            return kategori
        else:
            print(Fore.RED + "Geçersiz kategori! Lütfen 1, 2, 3 veya 4 seçiniz.")



def yonetici_girisi():
    print(Fore.MAGENTA + "***************************************************")
    print(Fore.YELLOW + "           Yönetici giriş işlemleri.               ")
    print(Fore.MAGENTA + "***************************************************")

    username_input = input(Fore.CYAN + "Kullanıcı Adı: ")
    password_input = input(Fore.CYAN + "Şifre: ")

    if cheek(username_input, password_input):
        print(Fore.GREEN + "Yönetici girişi başarılı!")
        while True:
            kategori = kategori_sec()
            if kategori == 1:  # Teknoloji
                print(Fore.BLUE + "\nAlt Kategoriler:")
                print(Fore.CYAN + "1 : Telefon")
                print(Fore.CYAN + "2 : Bilgisayar")

                secim = get_integer_input(Fore.CYAN + "Hangi alt kategoriye ürün eklemek istiyorsunuz (1): ")
                if secim == 1:
                    try:
                        id = input(Fore.YELLOW + "Ürün ID: ")
                        name = input(Fore.YELLOW + "Telefon Adı: ")
                        price = get_integer_input(Fore.YELLOW + "Fiyat: ")
                        amount = get_integer_input(Fore.YELLOW + "Miktar: ")
                        warranty = get_integer_input(Fore.YELLOW + "Garanti Süresi: ")
                        ram = get_integer_input(Fore.YELLOW + "RAM: ")
                        storage = get_integer_input(Fore.YELLOW + "Depolama: ")
                        fiveGsupport = get_choice_input(
                            Fore.YELLOW + "5G Desteği Var mı? (E/H): ", ["e", "h"]
                        )
                        numberofCameras = get_integer_input(Fore.YELLOW + "Kamera Megapiksel: ")
                        fastCharging = get_choice_input(
                            Fore.YELLOW + "Hızlı Şarj Desteği Var mı? (E/H): ", ["e", "h"]
                        )

                        new_phone = Phone(
                            id, name, price, amount, warranty, ram, storage,
                            fiveGsupport, numberofCameras, fastCharging
                        )
                        print(Fore.GREEN + f"{new_phone.get__name()} başarıyla eklendi!")
                    except Exception as e:
                        print(Fore.RED + f"Hata: {e}")

                elif secim == 2:
                    try:
                        id = input(Fore.YELLOW + "Ürün ID: ")
                        name = input(Fore.YELLOW + "Bilgisayar Adı: ")
                        price = get_integer_input(Fore.YELLOW + "Fiyat: ")
                        amount = get_integer_input(Fore.YELLOW + "Miktar: ")
                        warranty = get_integer_input(Fore.YELLOW + "Garanti Süresi: ")
                        ram = get_integer_input(Fore.YELLOW + "RAM: ")
                        storage = get_integer_input(Fore.YELLOW + "Depolama: ")

                        new_pc = Pc(id, name, price, amount, warranty, ram, storage)
                        print(Fore.GREEN + f"{new_pc.get__name()} başarıyla eklendi!")
                    except Exception as e:
                        print(Fore.RED + f"Hata: {e}")
                else:
                    print(Fore.RED + "Geçersiz seçim!")
            elif kategori == 2:
                print(Fore.BLUE + "\nAlt Kategoriler:")
                print(Fore.CYAN + "1 : Parfüm")
                print(Fore.CYAN + "2 : Şampuan")

                secim = get_integer_input(Fore.CYAN + "Hangi alt kategoriye ürün eklemek istiyorsunuz (1): ")
                if secim == 1:
                    try:
                        id = input(Fore.YELLOW + "Ürün ID: ")
                        name = input(Fore.YELLOW + "Ürün Adı: ")
                        price = get_integer_input(Fore.YELLOW + "Fiyat: ")
                        amount = get_integer_input(Fore.YELLOW + "Miktar: ")
                        expiration_date = input(Fore.YELLOW + "Son Kullanma Tarihi: ")
                        brand = input(Fore.YELLOW + "Marka: ")
                        volume = get_integer_input(Fore.YELLOW + "Ürün Hacmi: ")
                        gender_target = get_choice_input(
                            Fore.YELLOW + "Cinsiyet Hedefi (E/K): ", ["e", "k"]
                        )
                        alcohol_content = get_choice_input(
                            Fore.YELLOW + "Alkol Durumu (içerir/içermez): ", ["içerir", "içermez"]
                        )

                        new_perfume = Perfume(
                            id, name, price, amount, expiration_date, brand, volume, gender_target, alcohol_content
                        )
                        print(Fore.GREEN + f"{new_perfume.get__name()} başarıyla eklendi!")
                    except Exception as e:
                        print(Fore.RED + f"Hata: {e}")
                elif secim == 2:
                    try:
                        id = input(Fore.YELLOW + "Ürün ID: ")
                        name = input(Fore.YELLOW + "Ürün Adı: ")
                        price = get_integer_input(Fore.YELLOW + "Fiyat: ")
                        amount = get_integer_input(Fore.YELLOW + "Miktar: ")
                        expiration_date = input(Fore.YELLOW + "Son Kullanma Tarihi: ")
                        brand = input(Fore.YELLOW + "Marka: ")
                        paraben = get_choice_input(
                            Fore.YELLOW + "Koruyucu İçeriyor mu? (E/H): ", ["e", "h"]
                        )
                        hair_type = input(Fore.YELLOW + "Saç Tipi: ")
                        volume = get_integer_input(Fore.YELLOW + "Ürün Hacmi: ")

                        new_shampoo = Shampoo(
                            id, name, price, amount, expiration_date, brand, paraben, hair_type, volume
                        )
                        print(Fore.GREEN + f"{new_shampoo.get__name()} başarıyla eklendi!")
                    except Exception as e:
                        print(Fore.RED + f"Hata: {e}")
                else:
                    print(Fore.RED + "Geçersiz seçim!")
            elif kategori == 3:
                pass
            else:
                break
    else:
        print(Fore.RED + "Yönetici girişi başarısız! Tekrar deneyiniz.")



def kullanici_girisi():
    print(Fore.MAGENTA + "***************************************************")
    print(Fore.YELLOW + "             Kullanıcı giriş işlemleri.             ")
    print(Fore.MAGENTA + "***************************************************")
    while True:
        print(" ")
        secim = get_choice_input(Fore.CYAN + "Kayıtlı kullanıcı mısınız? (E/H): ", ["E", "H"])
        print(" ")
        if secim == "H":
            new_username = input(Fore.YELLOW + "Yeni Kullanıcı Adı: ")
            new_password = input(Fore.YELLOW + "Yeni Şifre: ")
            add_user(new_username, new_password)
            print(Fore.GREEN + "Kullanıcı başarıyla eklendi!")
            break
        elif secim == "E":
            username_input = input(Fore.CYAN + "Kullanıcı Adı: ")
            password_input = input(Fore.CYAN + "Şifre: ")

            if cheek_paswword(username_input, password_input):
                print(Fore.GREEN + "Kullanıcı girişi başarılı!")
                customer1 = customer("Ahmet", "ahmet@gmail.com", "Malatya", "085067055", [])

                while True:
                    print(Fore.BLUE + "\nİşlem Seçiniz:")
                    print(Fore.CYAN + "1 : Kategori Seçiniz")
                    print(Fore.CYAN + "2 : Sepete Git")
                    print(Fore.RED + "3 : Çıkış")
                    islem = get_integer_input(Fore.CYAN + "Seçiminiz: ")

                    if islem == 1:
                        print(" ")
                        kategori = kategori_sec()
                        if kategori == 1:  # Teknoloji
                            while True:
                                print(" ")
                                print(Fore.YELLOW + "Alt Kategoriler:")
                                print(Fore.CYAN + "1 - Telefon")
                                print(Fore.CYAN + "2 - Bilgisayar")
                                print(Fore.RED + "3 - Geri")
                                alt_kategori = get_integer_input(Fore.CYAN + "Seçiminiz: ")
                                print(" ")
                                if alt_kategori == 1:
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
                                            print(Fore.YELLOW + f"{i}. {phone.get__name()}")
                                        secim = get_integer_input(Fore.CYAN + "Sepete eklemek istediğiniz ürünü seçiniz: ")
                                        if 1 <= secim <= len(Phones):
                                            customer1.add_product(Phones[secim - 1])
                                            print(Fore.GREEN + "Ürün sepete eklendi!")
                                        else:
                                            print(Fore.RED + "Geçersiz seçim!")
                                    except FileNotFoundError:
                                        print(Fore.RED + "Ürün dosyası bulunamadı!")
                                elif alt_kategori == 2:
                                    Pclist = []
                                    try:
                                        df = pd.read_excel("Pc_urunleri.xlsx")
                                        for _, row in df.iterrows():
                                            pc = Pc(row["id"], row["name"], row["price"], row["amount"],
                                                    row["warranty"], row["ram"], row["storage"])
                                            Pclist.append(pc)

                                        for i, pc in enumerate(Pclist, start=1):
                                            print(Fore.YELLOW + f"{i}. {pc.get__name()}")
                                        secim = get_integer_input(Fore.CYAN + "Sepete eklemek istediğiniz ürünü seçiniz: ")
                                        if 1 <= secim <= len(Pclist):
                                            customer1.add_product(Pclist[secim - 1])
                                            print(Fore.GREEN + "Ürün sepete eklendi!")
                                        else:
                                            print(Fore.RED + "Geçersiz seçim!")
                                    except FileNotFoundError:
                                        print(Fore.RED + "Ürün dosyası bulunamadı!")
                                elif alt_kategori == 3:
                                    break
                        elif kategori == 2:
                            print(Fore.YELLOW + "Alt Kategoriler:")
                            print(Fore.CYAN + "1 - Parfüm")
                            print(Fore.CYAN + "2 - Şampuan")
                            print(Fore.RED + "3 - Geri")
                            alt_kategori = get_integer_input(Fore.CYAN + "Seçiminiz: ")
                            if alt_kategori == 1:
                                Perfumes = []
                                try:
                                    df = pd.read_excel("Parfume_urunleri.xlsx")
                                    for _, row in df.iterrows():
                                        parfum = Perfume(row["id"], row["name"], row["price"], row["amount"],
                                                         row["expiration_date"], row["brand"], row["volume"],
                                                         row["gender_target"], row["alcohol_content"])
                                        Perfumes.append(parfum)

                                    for i, parfum in enumerate(Perfumes, start=1):
                                        print(Fore.YELLOW + f"{i}. {parfum.get__name()}")
                                    secim = get_integer_input(Fore.CYAN + "Sepete eklemek istediğiniz ürünü seçiniz: ")
                                    if 1 <= secim <= len(Perfumes):
                                        customer1.add_product(Perfumes[secim - 1])
                                        print(Fore.GREEN + "Ürün sepete eklendi!")
                                    else:
                                        print(Fore.RED + "Geçersiz seçim!")
                                except FileNotFoundError:
                                    print(Fore.RED + "Ürün dosyası bulunamadı!")
                    elif islem == 2:
                        print(Fore.BLUE + "Sepet işlemleri...")
                    elif islem == 3:
                        print(Fore.RED + "Çıkış yapılıyor...")
                        break
                    else:
                        print(Fore.RED + "Geçersiz seçim!")
            else:
                print(Fore.RED + "Giriş yapılamadı. Kullanıcı adı veya şifre hatalı! Tekrar deneyiniz.")


def main():
    while True:
        print("\n1 : Yönetici Girişi")
        print("2 : Kullanıcı Girişi")
        print("3 : Çıkış")
        print(" ")
        giris = get_integer_input("Seçiniz (1-3): ")
        if giris == 1:
            yonetici_girisi()
        elif giris == 2:
            kullanici_girisi()
        elif giris == 3:
            print("Programdan çıkılıyor...")
            return

        else:
            print("Geçersiz seçim! Lütfen 1, 2 veya 3 seçiniz.")


if __name__ == "__main__":
        main()
