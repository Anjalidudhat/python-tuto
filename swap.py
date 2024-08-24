def swap(x,y):
    print("before swapping a:", x)
    print("After swapping b:", y)
    x,y = y,x
    return x,y
    
a = int(input("Enter value:"))
b = int(input("Enter value:"))

a,b = swap(a,b)

print("After swapping:",a)
print("After swapping:",b)