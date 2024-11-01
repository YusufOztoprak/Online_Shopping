import Personal_Care
class Shampoo(Personal_Care):
    Shampoo_list = []

    def __init__(self, name, price,amount,Id,expiration_date,brand,paraben,hairType,volume):
        super().__init__(name,price,amount,expiration_date,Id,brand)
        self.paraben = paraben
        self.hairType = hairType
        self.volume = volume

    def isSuitableforHairType(self,hairType):
        if(hairType.lower()  == self.hairType.lower()): return "This shampoo is suitable for your hair"
        else:
            return "This shampoo is not suitable for your"
    
    def getParaben(self):
        return self.paraben
    
    def getHairType(self):
        return self.hairType
    
    def getVolume(self):
        return self.volume
    
    def setParaben(self,paraben):
        self.paraben = paraben
        
    def setHairType(self,hairType):
        self.hairType = hairType
        
    def setVolume(self,volume):
        self.volume = volume

    def addShampoo(self):
        Shampoo.Shampoo_list.append(self)

    @classmethod
    def list_shampoos(cls):
        return cls.Shampoo_list

    @classmethod
    def find_by_brand(cls, brand):
        return [shampoo for shampoo in cls.Shampoo_list if shampoo.brand.lower() == brand.lower()]

    def __str__(self):
        return (f"Shampoo(Name: {self.name}, Price: {self.price}, Amount: {self.amount}, "
                f"ID: {self.Id}, Expiration Date: {self.expiration_date}, Brand: {self.brand}, "
                f"Paraben: {self.paraben}, Hair Type: {self.hairType}, Volume: {self.volume}ml)")


