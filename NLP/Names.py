#! usr/bin/env Python
# coding = utf-8

import nltk
names = nltk.corpus.names

cfd = nltk.ConditionalFreqDist(
    (fileid, name[-1])
    for fileid in names.fileids()
    for name in names.words(fileid))

cfd.plot()
