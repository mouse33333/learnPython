#! usr/bin/env Python
# coding=utf-8

print "哈哈哈"

from sys import argv
import sys

a, b = argv

b = raw_input("b is equial to: ")

print "This script is called: ", a
print "Your first variable is: ", b
print "参数个数为：", len(sys.argv)
print "参数列表为：", str(sys.argv)
#print "Your second variable is: ", second
#print "Your third variable is: ", third
