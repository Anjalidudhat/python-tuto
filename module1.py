# person1 = {
#     "name": "anjali",
#     "age": 24,
#     "country": "USA"
# }

# import mymodule

# a = mymodule.person1["age"]

# print(a)


# from sub import submarks

# submarks()

import json

person1 = {
    "name": "anjali",   
    "age": 24,
    "country": "USA"
}

a = json.dumps(person1)

lo = json.loads(a)

litss = list(lo.values())

print(litss)