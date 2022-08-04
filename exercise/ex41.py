#! usr/bin/env Python
# coding=utf-8

from sys import exit
from random import randint

def death():
    quips = "hahahaha, you died"
    print quips
    exit(1)

def princess_lives_here():
    print "you found the princess"
    choice = raw_input("what's your choice: ")
    if choice < 0 or choice >= 0:
        return "big_iron_gate"

def big_iron_gate():
    print "you found the big iron gate"
    choice2 = raw_input("what's your choice: ")
    if choice2 > 0 or choice2 <= 0:
        return "death"

rooms = {
    "death": death,
    "princess_lives_here": princess_lives_here,
    "big_iron_gate":big_iron_gate
}

def runner(map, start):
    next = start
    while True:
        room = map[next]
        print room
        print "\n--------"
        next = room() #important

runner(rooms, "princess_lives_here")
