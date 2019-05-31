from orderitem import orderitem
from menuitem import Item
from payment import Payment

class Order():
    def __init__(self):
        self.orderitems=[]
    
    def addorderitems(self, customerorder):
        self.orderitems.append(customerorder)
    
    def calctotal(self):
        totalcost=0
        for order in self.orderitems:
            totalcost=totalcost + order.getitem().itemprice * order.quantity
                    
        payment=Payment(totalcost)

        return payment



