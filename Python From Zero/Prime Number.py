#! usr/bin/env Python
# coding = utf-8

def prime_number(x):
    for i in range(2, (x+1)/2):
        if x % i == 0:
            return x, 'can be divided by', i, x, 'is not a prime number'
    return x, 'is a prime number'

print prime_number(454544567)
