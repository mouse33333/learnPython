#! usr/bin/env Python
# coding=utf-8

ten_things = "apples oranges crows tlephone light suger"

print "Wait there's not 10 things in that list, let's fix that."

stuff = ten_things.split(" ")
more_stuff = ["day", "night", "song", "frisbee", "corn", "banana", "girl", "boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "adding: ", next_one
    stuff.append(next_one)
    print "there's %d items now." % len(stuff)

print "There we go: ", stuff
print "Let's do some thins with stuff."

print stuff[1]
print stuff[-1]
print stuff.pop()
print " ".join(stuff)
print "#".join(stuff[3:5])
