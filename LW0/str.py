import math

a = input()

print(a, type(a))

if a == "pi":
    a = math.pi
else:
    a = float(a)
print(a, type(a))