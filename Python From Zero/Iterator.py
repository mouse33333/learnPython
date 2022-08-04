#! /usr/bin/env Python
# coding = utf-8

class MyRange(object):
    def __init__(self, n):
        self.i = 1
        self.n = n
    def __iter__(self):
        return self
    def next(self):
        if self.i < self.n:
            i = self.i
            self.i = self.i + 1
            return i
        else:
            raise StopIteration()

if __name__ == "__main__":
    x = MyRange(8)
    print list(x)

class Fibs(object):
    def __init__(self, max):
        self.max  = max
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def next(self):
        fib = self.a
        if fib > 1000:
            print fib
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib

if __name__ == "__main__":
    fibs = Fibs(10000)
    print list(fibs)
