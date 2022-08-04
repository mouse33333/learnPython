lst = ['a','b','c','d']
for i in lst:
    print i

lst_it = iter(lst)

while True:
    print lst_it.next()
