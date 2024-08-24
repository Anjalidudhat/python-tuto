def fibo(n, t1, t2):
    if n <= 0:
        return
    nextterm = t1 + t2
    print(nextterm, end=" ")
    fibo(n - 1, t2, nextterm)  # Corrected order and decrement

def print_fibo(n):
    if n < 1:
        print("invalid input")
    elif n == 1:
        print("0")
    elif n == 2:
        print("0 1")
    else:
        print("0 1", end=" ")
        fibo(n - 2, 0, 1)  # Corrected call to fibo and adjusted parameters

print_fibo(10)
