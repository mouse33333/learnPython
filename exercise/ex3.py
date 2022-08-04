# coding: utf-8

print "你好"

pow2 = []
for i in range(1,10):
    pow2.append(pow(i,2))
print pow2

mybad = [' abc',' dfsaf ']
mybad2 = [i.strip() for i in mybad]
print mybad2

while 1:
    print "this is a division programme"
    c = raw_input("input 'c' to continue, otherwise logout:" )
    if c == "c":
        a = raw_input("first number:")
        b = raw_input("second number:")
        try:
            print float(a)/float(b)
            print "****************"
        except Exception, e:
            print e
            print "****************"
    else:
        break
