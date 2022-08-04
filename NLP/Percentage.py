#! usr/bin/env Python
# coding = utf-8

from nltk.book import *

def percent2(word, text):
    fdist = FreqDist(text)
    f_word = fdist[word]
    per = float(f_word)/len(text) #key step: float
    return "%.5f%%" %(per*100)

print percent2("me", text1)
