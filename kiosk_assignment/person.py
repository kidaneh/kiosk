class Person():
    def __init__(self, id, name, lname, phone ):
        self.id=id
        self.name=name
        self.lname=lname
        self.phone=phone

    def getname(self):
        return self.name
    
    def getlname(self):
        return self.lname
    
    def getphone(self):
        return self.phone

    def __str__(self):
       # return "Full name is" + self.name +" " + self.lname
       return self.name

