from person import Person
class Employee():
    def __init__(self, id, name, lname, phone, shift, salary):
        self.id=id
        self.name=name
        self.lname=lname
        self.phone=phone
        self.shift=shift
        self.salary=salary
    
    def getsalary(self):
        return self.salary
    
    def __str__(self):
        return super(Employee, self).__str__() + ","+ self.salary