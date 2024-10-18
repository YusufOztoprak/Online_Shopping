class Telefon:
    def __init__(self,marka, fiyat, adet):
        self.marka = marka
        self.fiyat = fiyat
        self.adet = adet

    def get_info(self):
        return f"marka:{self.marka}, fiyat:{self.fiyat}, telefon adeti: {self.adet}"


class Magaza:
    def __init__(self):
        self.Telefonlar =[]


    def telefonekle(self,telefon):
        self.Telefonlar.append(telefon)# 2-burda aşağıda kulalnıcıdan aldığımız bilgilere göre oluşturduğumuz telefon nesnesini Telefonlar listesine atıyoruz
        print(f"{telefon.marka} markalı telefon mağazada stokalndı")# telefon bir nesne telefen.marka ise nesnenin isim özelliği

    def telefonsil(self, marka):
        for telefon in self.Telefonlar: # 3 - burdaki döngüde biz nesneler üzerinde dönüyoruz her nesnenin Telefon sınıfına ait özllikleri var
            # bu yüzden burdaki nesnenin özelliklerine erişebiliriz.
            if telefon.marka == marka:
                self.Telefonlar.remove(telefon)# hatanın sebebi burda nesneyi değil de nessnenin özelliğini çıkarmaya çalışmam
                print(f"{marka} markalı telefon stoklardan çıkarıldı.")
                return
        print(f"{marka} markalı bir telefon stoklarda mevcut değildir..")

    def listele(self):
        if not self.Telefonlar:
            print("stoklarda hiç telefon yok")
        else:
            print("stoklardaki telefonlar:")
            for telefon in self.Telefonlar:
                print(telefon.get_info())
    def durumguncelle(self,marka,marka1, yenifiyat,yeniadet):
        for telefon in self.Telefonlar:
            if telefon.marka == marka:
                telefon.marka = marka1
                telefon.fiyat = yenifiyat
                telefon.adet = yeniadet
                print(f"{marka} markalı telefonun bilgileri güncellendi.")
                return
        print(f"mağazada {marka} markalı bir telefon bulunamamıştır.")

    def telefonsat(self,marka):
        if not self.Telefonlar:
            print("stokta telefon yok")
        else:
            for telefon in self.Telefonlar:
                if telefon.marka == marka:
                    if telefon.adet > 0:
                        telefon.adet = telefon.adet - 1
                    else:
                        print(f"{marka} markalı telefonun stoğu tükenmiş")






def magaza_sistem():
    magaza = Magaza()

    while True:
        print("\n--- Mağaza Yönetim Sistemi ---")
        print("1. telefon Ekle")
        print("2. telefon Sil")
        print("3. telofonları Listele")
        print("4. bilgi güncelleme")
        print("5. satış yap")
        print("6. Çıkış")

        secenek = input("bir seçenek giriniz:")


        if secenek == "1":
            marka = input("telefon markası:")
            fiyat = input("telefonun fiyatı:")
            adet = int(input("telefon adeti:"))
            telefon = Telefon(marka, fiyat, adet) # 1-burda bir Telefonlar sınıfından bir telefon adlı nesne oluşturuyoruz.
            magaza.telefonekle(telefon)

        elif secenek == "2":
            if not magaza.Telefonlar:
                print("stokta hiç telefon mevcut değilir...")
            else:
                marka = input("silincek telefonun markası:")
                magaza.telefonsil(marka)

        elif secenek == "3":
            magaza.listele()

        elif secenek == "4":
            if not magaza.Telefonlar:
                print("mağazada hiç telefon yok")
            else:
                marka = input("hangi markayı güncellemk istiyorsunuz:")
                marka1 = input("telefonun yeni adı:")
                fiyat = input("güncel fiyatı giriniz:")
                adet = int(input("güncel adeti giriniz lütfen:"))
                magaza.durumguncelle(marka,marka1,fiyat,adet)
        elif secenek == "5":
            if not magaza.Telefonlar:
                print("stokta telefon yok")
            else:
                marka = input("satılacak telefon:")
                magaza.telefonsat(marka)
                #print(f"{marka} markalı telefonun güncel adeti: {telefon.adet} ")
        elif secenek == "6":
            print("sistemden çıkış yapılıyor...")
            break

        else:
            print("Geçersiz seçenek. lütfen tekrar deneyin")
magaza_sistem()