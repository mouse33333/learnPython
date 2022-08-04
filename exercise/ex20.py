#! usr/bin/env Python
# coding=utf-8

from sys import argv

script, file_name = argv

def print_line(line_count, f):
    print line_count, f.readlines()[line_count]

current_file = open(file_name)

line_count = 1
print_line(line_count, current_file)

current_file.seek(0) #key!!

line_count = 10
print_line(line_count, current_file)
