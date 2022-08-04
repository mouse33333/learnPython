#!/usr/bin/env Python
# coding = utf-8

def fib(n):
    """""
    this is Fibonacci by
    """""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print fib(5)
