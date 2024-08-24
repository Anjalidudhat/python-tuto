a = (5, 20, 3, 7, 6, 8)
 
# printing original tuple
print("The original tuple is : " + str(a))
 
# initializing K 
K = 2
 
# Maximum and Minimum K elements in Tuple
# Using sorted() + loop
res = []
a = list(sorted(a))
 
for idx, val in enumerate(a):
    if idx < K or idx >= len(a) - K:
        res.append(val)
res = tuple(res)
 
# printing result 
print("The extracted values : " + str(res)) 