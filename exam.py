def is_prime(num):
     if num <= 1:
       return False

     for i in range(2,num//2 + 1):
         if(num % i) == 0:
           return False

     return True

number = 11
if is_prime(number):
        print(number, "is a prime number")
else:
  print(number, "is not a prime number")
       