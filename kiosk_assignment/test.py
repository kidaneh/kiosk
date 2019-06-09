import unittest
from menuitem import Item
from orderitem import orderitem
from orders import Order
from payment import Payment
from person import Person

class itemTest(unittest.TestCase):
    def setUp(self):
        self.item=Item(1, "Pissa", 5.00)

    def test_string(self):
        self.assertEqual(str(self.item), self.item.itemname)
    
    def test_getitemid(self):
        self.assertEqual(self.item.getitemid(), 1 )
    
    def test_getItemnumber(self):
        self.assertEqual(self.item.getitemPrice(), 5.00)
    
class orderitemtest(unittest.TestCase):
    def setUp(self):
        self.item=Item(1, "Pissa", 5.00)
        self.order=orderitem(self.item, 3)
    
    def test_getquantity(self):
        self.assertEqual(self.order.getquantity(), 3)
    
    def test_getitemid(self):
        item=self.order.getitem()
        self.assertEqual(str(item), "Pissa" )

class persontest(unittest.TestCase):
    def setUp(self):
        self.person=Person(1, "Kidane", "Gidey", "7121909")

    def test_string(self):
        self.assertEqual(str(self.person), self.person.name)
    
    def test_getphone(self):
        self.assertEqual(self.person.getphone(), "7121909" )

class ordertest(unittest.TestCase):
    def setUp(self):
        self.item1=Item(1, "Hamberger", 2.00)
        self.item2=Item(2,"Coca cola", 1.00)

        self.orderitem1=orderitem(self.item1, 2)
        self.orderitem2=orderitem(self.item2, 3 )

        self.order=order()
        self.order.addorderitems(self.orderitem1)
        self.order.addorderitems(self.orderitem2)
    
    def test_calculatebill(self):
        payement=self.order.calctotal()
        self.assertEqual(str(payement), "Thank you for purchasing from our store. Total payement is 7 ")


    
    





        

