import  hashlib
import json

def hash_password(password):
    has_p = hashlib.sha256(password.encode())
    return has_p.hexdigest()


veri = [
    {
        "username": "user1",
        "password": hash_password("memet123")
    },
    {
        "username": "user2",
        "password": hash_password("yusuf123")
    }
]

with open('veri.json','w') as  json_file:
    json.dump(veri,json_file)


def cheek_paswword(username, password):
    with open('veri.json', 'r') as json_file:
        kullanicilar = json.load(json_file)


    for kullanici in kullanicilar:
        if kullanici["username"] == username:
            hashed_input_password = hash_password(password)
            if hashed_input_password == kullanici["password"]:
                return True
            else:
                return False
    return False


username_input = input("kullanıcı adı:")
password_input = input("kullanıcı şifresi:")

dogru = cheek_paswword(username_input,password_input)

