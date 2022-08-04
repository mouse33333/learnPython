#pay attention to the source of the file
import fileinput
for line in fileinput.input('/Users/Arthur/learnPython/131.txt'):
    print line,

#for
f = open('/Users/Arthur/learnPython/131.txt')
for line in f:
    print(line)


#seek & tell
with open('/Users/Arthur/learnPython/131.txt') as f:
    print f.readline(),
    print f.readline(),
    f.seek(0)
    print f.readline(),
    print f.tell()
