class Complex:

    def __init__(self,realpart,imagpart):
        self.realpart = realpart
        self.imagpart = imagpart


x = Complex(3.0, -4.5)
print(x.imagpart,x.realpart)