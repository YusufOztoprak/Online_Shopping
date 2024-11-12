import hashlib
import json


def hash_password(password):
    has_p = hashlib.sha256(password.encode())
    return has_p.hexdigest()


veri = [
    {
        "username": "memet",
        "password": hash_password("memet123")
    },
    {
        "username": "yusuf",
        "password": hash_password("yusuf123")
    }
]

with open('yönetici.json', 'w') as json_file:
    json.dump(veri, json_file)


def cheek(username, password):
    with open('yönetici.json', 'r') as json_file:
        yoneticiler = json.load(json_file)

    for yonetici in yoneticiler:
        if yonetici["username"] == username:
            hashed_input_password = hash_password(password)
            if hashed_input_password == yonetici["password"]:
                return True
            else:
                return False
    return False

