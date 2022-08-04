#! ust/bin/env Python
# coding = utf-8

from nltk.book import *

fdist = FreqDist(text1)

fdist.items()

print fdist.max()
print fdist[3]
print fdist.freq(3)
print fdist['monstrous']
print fdist.N()
fdist.plot(50, cumulative = True)


