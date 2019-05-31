from menuitem import Item
    
class orderitem():
    def __init__(self, item, quantity):
        self.item=item
        self.quantity=quantity
    
    def getitem(self):
        return self.item
    
    def getquantity(self):
        return self.quantity
    
