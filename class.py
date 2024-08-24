class Employee:

    increment = 1.5

    def __init__(self, fname,lname, salary):

        self.fname = fname
        self.lname = lname
        self.salary = salary

    def increase(self):
        self.salary = int(self.salary * Employee.increment)

    @classmethod
    def from_str(cls,emp_string):
        fname,lname,salary = emp_string.split("-")
        return cls(fname,lname,salary)
    

    @staticmethod
    def isopen(day):
        if day == "sunday":
            return False
        else:
            return True
        
        
class programmer(Employee):
    def __init__(self,fname,lname, salary,proglan,exp):
        super().__init__(fname,lname,salary)
        self.proglan = proglan
        self.exp = exp


harry = programmer('harry', 'jackson', 99000, 'python', '5 years')
print(harry.proglan)
        
    # shubham = Employee('shubham', 'jackpot', 88000)
    # print(Employee.isopen('sunday'))

# anjali = Employee ('anjali','dudhat',50000)
# panisha = Employee ('panisha','dudhat',50000)
# lovish = Employee.from_str("lovish-jackpot-50000")

        
# print(anjali.fname,panisha.lname)
# print(anjali.salary)
# anjali.increase()
# print(anjali.salary)