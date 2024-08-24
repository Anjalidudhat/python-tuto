# you can use classmethod 

@classmethod
def from_str(cls,emp_string):
    fname,lname,salary = emp_string.split("-")
    return cls(fname,lname,salary)


lovish = Employee.from_str("lovish-jackpot-70000")
    