#!/usr/bin/env Python
# coding = utf-8

__metaclass__ = type

class Person:
    def __init__(self):
        self.height = 160
    def about(self, name):
        print "{} is about {}".format(name, self.height)

class Girl(Person):
    def __init__(self):
        self.breast = 60
        super(Girl, self).__init__()
    def about(self, name):
        print "{} is about {} and her breast is {}".format(name, self.height, self.breast)
        super(Girl, self).about(name)

if __name__ == "__main__":
    cang = Girl()
    cang.about("WangGuNiang")
