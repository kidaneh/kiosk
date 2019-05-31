from person import Person
class Customer():
    def __init__(self, id, name, lname, phone, memid, memstatus):
        self.id=id
        self.name=name
        self.lname=lname
        self.phone=phone
        self.memid=memid
        self.memstatus=memstatus
    
    def getmembershpid(self):
        return self.memid
    
    def getmembershipstaus(self):
        return self.memstatus

    def __str__(self):
        return super(Customer, self).__str__() + ","+ self.salary