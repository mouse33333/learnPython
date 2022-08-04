#! usr/bin/env Python
# coding=utf-8

from sys import exit
from random import randint

class Game:
    def __init__(self, start): #定义了这个类的默认参数传什么
        self.quips = ["hahaha, you died"]
        self.start = start

    def death(self):
        print self.quips[0]
        exit(1)

    def princess_lives_here(self):
        print "you found the princess"
        choice = raw_input("what's your choice: ")
        if choice < 0 or choice >= 0:
            return "big_iron_gate"#返回的是函数名称，不是函数本身

    def big_iron_gate(self):
        print "you found the big iron gate"
        choice2 = raw_input("what's your choice: ")
        if choice2 > 0 or choice2 <= 0:
            return "death" #important

    def play(self):
        next = self.start
        while True:
            print "\n--------"
            room = getattr(self, next) #因为是类的实例，所以要用getattr来获取实例的属性
            next = room() #（）的作用是让函数运行起来

a_game = Game("princess_lives_here")
a_game.play()
