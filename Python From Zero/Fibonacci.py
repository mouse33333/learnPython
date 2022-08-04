a1 = 1
a2 = 1
for n in range(49):
    a1 = a1 + a2
    a2 = a1 + a2
print a2

a = 0
b = 1
for i in range(100):
    a,b = b, a+b
print a
