#!/usr/bin/env Python
# coding = utf-8

numbers = range(10)
new_numbers = []
lam = lambda x: x+3
for i in numbers:
    new_numbers.append(lam(i))

print new_numbers

lam2 = [lambda x:x, lambda x: x**2, lambda x:x**3, lambda x:x**4]
for i in lam2:
    print i(3),

print map(lam, numbers)
