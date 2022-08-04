#! usr/bin/env Python
# coding = utf-8

import copy

word = "egivrvonl"
print list(word)

target = ['abc', 'ab', 'cd', 'edf', 'efdf', 'effsdafs', 'reresdf', 'efsdaffwers', 'eg']
copy_target = copy.deepcopy(target)

for w2 in target:
    for w3 in list(w2):
        if w3 not in list(word):
            copy_target.remove(w2)
            break

print copy_target
