#!/usr/bin/env Python
# coding = utf-8
__metaclass__ = type
class Person:
    def speak(self):
        print "I love you"
    def setHeight(self, n):
        self.height = n
    def breast(self, n):
        self.breast = n
        print "my breast is %s." % self.breast

class Girl(Person):
    def setHeight(self):
        print "The height is 1.6m"

if __name__ == "__main__":
    cang = Girl()
    cang.setHeight()
    cang.speak()
    cang.breast = 90
