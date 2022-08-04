#! usr/bin/env Python
# coding=utf-8

from sys import argv

script, filename = argv

print "do you really want to delete %s?" % filename
print "if yes, please hit return."
print "if no, please type ctrl-c"
raw_input("?")

print "opening the file..."
file_txt = open(filename, "w")
print "truncating the file..."
file_txt.truncate()
print "done"

print "now I need more lines."
line1 = raw_input("line1: ")
#line2 = raw_input("line2: ")
#line3 = raw_input("line3: ")

print "now I'm going to write these into files."

#file_txt.write(%s+"\n"+%s+"\n"+%s) %(line1, line2, line3)

file_txt.write("{}".format(line1)) #fuckfuckfuck
file_txt.close()
