#!/usr/bin/env python
# coding = utf-8

'''this is the code from learn Python from scratch'''

__metaclass__ = type

class Animal:
    def __init__(self, name=""):
        self.name = name
    def talk(self):
        pass

class Cat(Animal):
    def talk(self):
        print "Meow!"

class Dog(Animal):
    def talk(self):
        print "Woof!"

a = Animal()
a.talk()

c = Cat()
c.talk()

d = Dog()
d.talk()
