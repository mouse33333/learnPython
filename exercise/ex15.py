#! usr/bin/env Python
# coding=utf-8

from sys import argv

script, file_name = argv

txt = open(file_name)

print "Here's your file: %r" % file_name
print txt.read()
txt.close()

print "I'll ask you to type it again:"
file_again = raw_input(">:")

txt_again = open(file_again)
print txt_again.read()
txt_again.close()
