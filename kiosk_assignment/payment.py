class Payment():
    def __init__(self, paymentamount):
        self.paymentamount=paymentamount
    
    def __str__(self):
        self.paymentamount=round(self.paymentamount, 2)

        response="Thank you for purchasing from our store. Total payement is " + str(self.paymentamount)
        return response
    
