class Math:
    def __init__(self,FirstNumber,SecondNumber):
        self.first_num = FirstNumber
        self.second_num = SecondNumber
        
    def add(self,x=0,y=0,z=0):
        sum=x+y+z
        print("Sum=",sum)
    
    def sub(self):
        sub = self.first_num - self.second_num
        print("Sub=",sub)
        
    def mul(self):
        mul=self.first_num * self.second_num
        print("Mul=",mul)
        
    def div(self):
        div=self.first_num / self.second_num
        print("Div=",div)
        
        
def main():
    calc=Math(10,5)
    
    calc.add(90,10,45)
    calc.sub()
    calc.mul()    
    calc.div()


main()
