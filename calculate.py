class calculate:

    def add(self, a ,b):
        return a + b
    
    def subsract(self, a, b):
        return a - b
    
    def multi(self,a, b):
        return a * b
    
    def division(self, a, b):
        if b != 0:
          return a / b
        else:
            return "can not divide by zero"
        
cal = calculate()

num1 = 10
num2 = 20

print(f"{num1} + {num2} = {cal.add(num1,num2)}")
print(f"{num1} - {num2} = {cal.subsract(num1, num2)}")
print(f"{num1} * {num2} = {cal.multi(num1, num2)}")
print(f"{num1} / {num2} = {cal.division(num1, num2)}")


    

        