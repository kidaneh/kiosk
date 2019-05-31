class Item():
    def __init__(self, itemid, itemname, itemprice):
        self.itemid=itemid
        self.itemname=itemname
        self.itemprice=itemprice
    
    def getitemName(self):
        return self.itemname
    
    def getitemid(self):
        return self.itemid
    
    def getitemPrice(self):
        return self.itemprice
    
    def __str__(self):
        return self.itemname
    


