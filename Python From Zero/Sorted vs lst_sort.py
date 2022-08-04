lst = [1,2,3,4,5,6,7,8,9,0]
b = lst.pop(0)
lst.append(b)
print lst

import random
lst = []
for i in range(40):
    lst.append(random.randint(0,100))

print lst

a = 0
for i in lst:
    a = a + i

print a

b = a/40.0
c = []
for i in lst:
    if i < b:
        c.append(i)
num = len(c)
# pay attention to sorted and lst.sort
c_order = sorted(c,reverse = True)

print b
print c
print c_order
print num
