abc = 'How are  you? My  friend.'
abc_no_space = abc.split(" ")
for i in abc_no_space:
    if i == '':
        abc_no_space.pop(abc_no_space.index(i))

print abc_no_space

result = ' '.join(abc_no_space)
print result


