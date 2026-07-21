class Complex:
    def __init__(self,real,image):
        self.real=real
        self.imag=image
    def __add__(self,num2):
        newreal=self.real+num2.real
        newimag=self.imag+num2.imag
        return Complex(newreal,newimag)
    def display(self):
        print(self.real,"i+",self.imag,"j")
c1=Complex(1,2)
c2=Complex(2,3)
c3=c1+c2
print(c3)