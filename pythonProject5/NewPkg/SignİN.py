import json
import hashlib
import os

# Şifreyi hashleyen fonksiyon
def hash_password(password):
    has_p = hashlib.sha256(password.encode())
    return has_p.hexdigest()

# Yeni kullanıcıyı JSON dosyasına ekleyen fonksiyon
def add_user(username, password):
    # Dosya mevcut değilse ya da boşsa boş bir liste başlat
    if not os.path.exists('veri.json') or os.path.getsize('veri.json') == 0:
        kullanicilar = []
    else:
        with open('veri.json', 'r') as json_file:
            kullanicilar = json.load(json_file)

    # Yeni kullanıcıyı hashlenmiş şifre ile ekle
    yeni_kullanici = {
        "username": username,
        "password": hash_password(password)
    }
    kullanicilar.append(yeni_kullanici)

    # Güncellenmiş kullanıcı listesini JSON dosyasına kaydet
    with open('veri.json', 'w') as json_file:
        json.dump(kullanicilar, json_file, indent=4)

    print(f"Yeni kullanıcı {username} başarıyla kaydedildi!")
"""import json
import hashlib
# Yeni kullanıcıyı JSON dosyasına ekleyen fonksiyon

def hash_password(password):
    has_p = hashlib.sha256(password.encode())
    return has_p.hexdigest()

def add_user(username, password):
    with open('veri.json', 'r') as json_file:
        kullanicilar = json.load(json_file)

    # Yeni kullanıcıyı hashlenmiş şifre ile ekle
    yeni_kullanici = {
        "username": username,
        "password": hash_password(password)
    }
    kullanicilar.append(yeni_kullanici)

    # Güncellenmiş kullanıcı listesini JSON dosyasına kaydet
    with open('veri.json', 'w') as json_file:
        json.dump(kullanicilar, json_file, indent=4)

    print(f"Yeni kullanıcı {username} başarıyla kaydedildi!")
"""