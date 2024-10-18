class user:
    def __init__(self, name, email, username,  password,  address):
        self.name = name
        self.email = email
        self.username = username
        self.password = password
        self.address = address

        """def get_Name(self):
            return self.name

        def get_Email(self):
            return self.email

        def get_UserName(self):
            return self.username


        def __get_Password(self):
            return self.__password

        def __get_address(self):
            return self.__address"""

        def displayinfo(self):
            return f"kullanıcı adı:{self.username}, email:{self.email},  adrress: {self.address}"

kullanici = user("yusuf", "fake@gmail.com", "cosefthegreate", "yusuf3131", "inönü akul hastanesi")

print(kullanici.email)













