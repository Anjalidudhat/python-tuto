import json

x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

y = json.dumps(x)

lo = json.loads(y)

# Convert dictionary items to a list of tuples
items_list = list(lo.items())

print(items_list)
