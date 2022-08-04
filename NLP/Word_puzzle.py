#! usr/bin/env Python
# coding = utf-8

# not endswith(s)
# must contain "r"
# must have a nine-letter word
# more than four
# each letter just once

import nltk
import copy

word_list = nltk.corpus.words.words()
word1 = "egivrvonl"
word_set = list(word1)

target = []

for w1 in word_list:
    if len(w1) >= 4:
        target.append(w1)

print "this is the first", len(target)

target1 = copy.deepcopy(target)

for w2 in target:
    for w3 in list(w2):
        if w3 not in word_set or "r" not in list(w2) or w2.endswith("s"):
            target1.remove(w2)
            break

print "this is the second", len(target1)

target2 = copy.deepcopy(target1)

for w3 in target1:
    w3_freq = nltk.FreqDist(w3)
    w3_set = w3_freq.items()
    for items in w3_set:
        if items[1] >= 2:
            target2.remove(w3)
            break

print set(target2)
print len(set(target2))

