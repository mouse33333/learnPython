#!/usr/bin/env python
# coding = utf-8

__metaclass__ = type

class ProtectMe():
    def __init__(self):
        self.me = "abcde"
        self.__name = "Python"
    @property
    def name(self):
        return self.__name

if __name__ == "__main__":
    p = ProtectMe()
    print p.me
    print p.name
