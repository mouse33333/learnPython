#! usr/bin/env Python
# coding=utf-8

from sys import argv
from os.path import exists

script, from_file, to_file = argv

#print "copying file from {}".format(from_file)

#from_data = open(from_file).read()

#print "the length of this file is {}".format(len(from_data))

#print "does the new file exist? {}".format(exists(to_file))
#print "ok, please press enter to continue or ctrl-c to abort."
#raw_input()
out_data = open(to_file, 'w').write(open(from_file).read())

print "done"




