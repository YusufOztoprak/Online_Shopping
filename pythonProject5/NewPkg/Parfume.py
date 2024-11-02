from Personal_Care import PersonalCare

class Perfume(PersonalCare):
    def __init__(self, name, price, amount, Id, expiration_date, brand, volume, gender_target, alcohol_content):
        super().__init__(name, price, amount, Id, expiration_date, brand)
        self.volume = volume
        self.gender_target = gender_target
        self.alcohol_content = alcohol_content
    def displayDetails(self):
        details = f"""
        Hacim: {self.volume}ml
        Hedef Cinsiyet: {self.gender_target}
        Alkol İçeriği: {self.alcohol_content}
        """
        print(details)

    def getVolume(self):
        return self.volume

    def setVolume(self, volume):
        self.volume = volume

    def getAlcoholContent(self):
        return self.alcohol_content

    def setAlcoholContent(self, alcohol_content):
        self.alcohol_content= alcohol_content

    def  getGenderTarget(self):
        return self.gender_target

    def setGenderTarget(self, gender_target):
        self.gender_target= gender_target

    def addParfume(self, parfume):
        self.parfumes.append(parfume)
