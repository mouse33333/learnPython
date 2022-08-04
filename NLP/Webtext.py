#! ust/bin/env Python
# coding = utf-8

from nltk.corpus import webtext

#for fileid in webtext.fileids():
 #   print fileid, "\n", webtext.raw(fileid)[:65], "\n"

import nltk
#from nltk.corpus import brown

#print brown.categories()

#news_text = brown.words(categories="news")
#fdist = nltk.FreqDist([w.lower() for w in news_text])

#words = ["who", "what", "why", "how", "where"]

#for w in words:
#    print w, ":", fdist[w]

from nltk.corpus import inaugural

cfd = nltk.ConditionalFreqDist(
    (target, fileid[:4])
    for fileid in inaugural.fileids()
    for w in inaugural.words(fileid)
    for target in ["america", "citizen"]
    if w.lower().startswith(target))
cfd.plot()
