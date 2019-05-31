from employee import Employee
from customer import Customer
from menuitem import Item
from orderitem import orderitem
from orders import Order
from payment import Payment



def setEmployee():
    e=Employee("10",'kidane','Haile',"124312","1st",1200)
    print (e.name)
    print(e.salary)
    

def setCustomer():
    c=Customer("10",'kidane','Haile',"124312",100,"Golden")
    print (c.name)
    print(c.memstatus)
    

def main():
    print ("employee name and salary")
    setEmployee()
    print("Customer name and status")
    setCustomer()

    item1=Item(1, 'Cheezeburger', 3.00)
    item2=Item(2, 'Orange Juice', 4.00)
    item3=Item(3, 'Milk', 5.00)

    orderitem1=orderitem(item1, 2)
    orderitem2=orderitem(item2, 3)
    orderitem3=orderitem(item3, 1)


    order=Order()
    order.addorderitems(orderitem1)
    order.addorderitems(orderitem2)
    order.addorderitems(orderitem3)

    payment=order.calctotal()
    print(payment)


main()

