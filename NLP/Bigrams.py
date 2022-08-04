#! usr/bin/env Python
# coding = utf-8

import nltk

def generate_model(cfdist, word, num=15):
    for i in range(num):
        word = cfdist[word].max()
        print word

text = nltk.corpus.genesis.words()
bigrams = nltk.bigrams(text)
cfd = nltk.ConditionalFreqDist(bigrams)
print cfd["living"]
generate_model(cfd, "living")


