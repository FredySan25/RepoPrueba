class Item():
    def __init__(self, sku):
        self.sku = sku
        
    def print_sku(self):
        print("The sku is " + self.sku)
        
class Garment():
    def __init__(self, section, type):
        self.section = section
        self.type = type
    
    def print_garment(self):
        print("The garment is in section {}, {}".format(self.section, self.type))
        
class Shirts(Item,Garment):
    def __init__(self, sku, section, type, name, color):
        self.name = name
        self.color = color
        Item.__init__(self, sku)
        Garment.__init__(self, section, type)
        
    def print_shirt(self):
        print(self.color + ", " + self.name + " on sale!")
        
Blouse = Shirts("00001", 43, "Tops", "Formal blouse", "White")

Blouse.print_sku()
Blouse.print_garment()
Blouse.print_shirt()