a = {
    "name": "anajli",
    "age" : 23,
    "gender": "female"
}

b = list(a.keys())
b.sort()
sorted_dict = {key: a[key] for key in b}

print(sorted_dict)  