from pythonProject5.NewPkg.Parfume import Perfume
from pythonProject5.NewPkg.Phone import Phone
from pythonProject5.NewPkg.customer import customer
from pythonProject5.NewPkg.cart import Cart
from pythonProject5.NewPkg.SignİN import add_user
from pythonProject5.NewPkg.Login import cheek_paswword
from pythonProject5.NewPkg.managment import cheek

import pandas as pd


def get_integer_input(prompt):
    """Kullanıcıdan tam sayı almak için güvenli giriş."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Hatalı giriş! Lütfen bir sayı giriniz.")


def get_choice_input(prompt, valid_choices):
    """Kullanıcıdan belirli bir seçim almak için güvenli giriş."""
    while True:
        choice = input(prompt).strip()
        if choice in valid_choices:
            return choice
        else:
            print(f"Hatalı giriş! Lütfen şu seçeneklerden birini seçiniz: {', '.join(valid_choices)}")


def kategori_sec():
    print("KATEGORİLER")
    while True:
        print("\nKategori Seçiniz:")
        print("1 : Teknoloji")
        print("2 : Kişisel Bakım")
        print("3 : Giyim")
        print("4: çıkış")
        kategori = get_integer_input("Seçiminiz (1-3): ")
        if kategori in [1, 2, 3, 4]:
            return kategori
        else:
            print("Geçersiz kategori! Lütfen 1, 2 veya 3 seçiniz.")


def yonetici_girisi():
    print("Yönetici giriş işlemleri.")

    username_input = input("Kullanıcı Adı: ")
    password_input = input("Şifre: ")
    if cheek(username_input, password_input):
        print("Yönetici girişi başarılı!")
        while(True):
            kategori = kategori_sec()
            if kategori == 1:  # Teknoloji
                print("\nAlt Kategoriler:")
                print("1 : Telefon")
                secim = get_integer_input("Hangi alt kategoriye ürün eklemek istiyorsunuz (1): ")
                if secim == 1:
                    try:
                        id = input("Ürün ID: ")
                        name = input("Telefon Adı: ")
                        price = get_integer_input("Fiyat: ")
                        amount = get_integer_input("Miktar: ")
                        warranty = get_integer_input("Garanti Süresi: ")
                        ram = get_integer_input("RAM: ")
                        storage = get_integer_input("Depolama: ")
                        fiveGsupport = get_choice_input("5G Desteği Var mı? (E/H): ", ["E".lower(), "H".lower()])
                        numberofCameras = get_integer_input("Kamera Megapiksel: ")
                        fastCharging = get_choice_input("Hızlı Şarj Desteği Var mı? (E/H): ", ["E".lower(), "H".lower()])

                        new_phone = Phone(
                            id, name, price, amount, warranty, ram, storage,
                            fiveGsupport, numberofCameras, fastCharging
                        )
                        print(f"{new_phone.get__name()} başarıyla eklendi!")
                    except Exception as e:
                        print(f"Hata: {e}")
                else:
                    print("Geçersiz seçim!")
            elif(kategori == 2):
                print("\nAlt Kategoriler:")
                print("1 : parfüm")
                secim = get_integer_input("Hangi alt kategoriye ürün eklemek istiyorsunuz (1): ")
                if secim == 1:
                    try:
                        id = input("Ürün ID: ")
                        name = input("ürün Adı: ")
                        price = get_integer_input("Fiyat: ")
                        amount = get_integer_input("Miktar: ")
                        expiration_date = get_integer_input("son kullanma tarihi:")
                        brand = input("marka:")
                        volume = get_integer_input("ürün hacmi:")
                        gender_target = get_choice_input("cinsiyet hedefi(E,K): ", ["E".lower(), "k".lower()])
                        alcohol_content =  get_choice_input("alkol durumu:(içerir, içermez)",["içerir".lower(), "içermez".lower()])


                        new_Parfume = Perfume(
                            id, name, price, amount,expiration_date,brand,volume,gender_target,alcohol_content)
                        print(f"{new_Parfume.get__name()} başarıyla eklendi!")
                    except Exception as e:
                        print(f"Hata: {e}")
                else:
                     print("Geçersiz seçim!")
            elif(kategori == 3):
                pass
            else:
                break

    else:
        print("Yönetici girişi başarısız! Tekrar deneyiniz.")



def kullanici_girisi():
    print("Kullanıcı giriş işlemleri.")
    while True:
        secim = get_choice_input("Kayıtlı kullanıcı mısınız? (E/H): ", ["E", "H"])
        if secim == "H":
            new_username = input("Yeni Kullanıcı Adı: ")
            new_password = input("Yeni Şifre: ")
            add_user(new_username, new_password)
            print("Kullanıcı başarıyla eklendi!")
            break
        elif secim == "E":
            username_input = input("Kullanıcı Adı: ")
            password_input = input("Şifre: ")

            if cheek_paswword(username_input, password_input):
                print("Kullanıcı girişi başarılı!")
                customer1 = customer("Ahmet", "ahmet@gmail.com", "Malatya", "085067055", [])

                while True:
                    print("\nİşlem Seçiniz:")
                    print("1 : Kategori Seçiniz")
                    print("2 : Sepete Git")
                    print("3 : Çıkış")
                    islem = get_integer_input("Seçiminiz: ")

                    if islem == 1:
                        kategori = kategori_sec()
                        if kategori == 1:  # Teknoloji
                            while True:
                                print("Alt Kategoriler:")
                                print("1 - Telefon")
                                print("2 - Bilgisayar")
                                print("3 - geri")
                                alt_kategori = get_integer_input("Seçiminiz: ")
                                if alt_kategori == 1:  # Telefon
                                    Phones = []
                                    try:
                                        df = pd.read_excel("telefon_urunleri.xlsx")
                                        for _, row in df.iterrows():
                                            telefon = Phone(row["id"], row["name"], row["price"], row["amount"], row["warranty"], row["ram"], row["storage"], row["fiveGsupport"], row["numberOfcameras"], row["fastCharging"]
                                            )
                                            Phones.append(telefon)

                                        for i, phone in enumerate(Phones, start=1):
                                            print(f"{i}. {phone.get__name()}")
                                        secim = get_integer_input("Sepete eklemek istediğiniz ürünü seçiniz: ")
                                        if 1 <= secim <= len(Phones):
                                            customer1.add_product(Phones[secim - 1])
                                            print("Ürün sepete eklendi!")
                                        else:
                                            print("Geçersiz seçim!")
                                    except FileNotFoundError:
                                        print("Ürün dosyası bulunamadı!")
                                elif alt_kategori == 2:
                                    pass
                                elif alt_kategori == 3:
                                    break
                        elif (kategori == 2):
                            print("Alt Kategoriler:")
                            print("1 - parfüm")
                            print("2 - şampuan")
                            alt_kategori = get_integer_input("Seçiminiz: ")
                            if alt_kategori == 1:  # Telefon
                                Perfumes = []
                                try:
                                    df = pd.read_excel("Parfume_urunleri.xlsx")
                                    for _, row in df.iterrows():
                                        parfum = Perfume(row["id"], row["name"], row["price"], row["amount"],
                                                         row["expiration_date"], row["brand"], row["volume"],
                                                         row["gender_target"], row["alcohol_content"])
                                        Perfumes.append(parfum)

                                    for i, parfum in enumerate(Perfumes, start=1):
                                        print(f"{i}. {parfum.get__name()}")
                                    secim = get_integer_input("Sepete eklemek istediğiniz ürünü seçiniz: ")
                                    if 1 <= secim <= len(Perfumes):
                                        customer1.add_product(Perfumes[secim - 1])
                                        print("Ürün sepete eklendi!")
                                    else:
                                        print("Geçersiz seçim!")
                                except FileNotFoundError:
                                    print("Ürün dosyası bulunamadı!")
                    elif islem == 2:
                        customer1.show_cart()
                        print("işlemler:")
                        print("1-sepeti göster:")
                        print("2-sepetten ürün sil:")
                        print("3-toplam tutarı göster:")
                        print("4-sepeti temizle")
                        print("5- geri dön")
                        while(True):
                            islem = int(input("hangi işlemi yapmak istiyorsunuz:"))
                            if (islem == 1):
                                customer1.show_cart()
                            elif (islem == 2):
                                customer1.show_cart()
                                sec = int(input("silmek istediğiniz ürünün numarası"))
                                customer1.remove_product(sec)
                            elif (islem == 3):
                                print(customer1.total_price())
                            elif (islem == 4):
                                customer1.clear_cart()
                            elif (islem == 5):
                                break
                    elif islem == 3:
                        print("Çıkış yapılıyor...")
                        break
                    else:
                        print("Geçersiz seçim!")
                break
            else:
                print("Giriş yapılamadı. Kullanıcı adı veya şifre hatalı! Tekrar deneyiniz.")


def main():
    while True:
        print("\n1 : Yönetici Girişi")
        print("2 : Kullanıcı Girişi")
        print("3 : Çıkış")
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
