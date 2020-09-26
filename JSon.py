import json

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])
f=open("JSon.py","r")
print(f)
print(f.read())
print(f.readline())
