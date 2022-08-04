#! usr/bin/env Python
# coding = utf-8

from nltk.corpus import stopwords
import nltk

def content_fraction(text):
    stopwords = nltk.corpus.stopwords.words("english")
    content = [w for w in text if w.lower() not in stopwords]
    return float(len(content))/len(text)

print content_fraction(nltk.corpus.reuters.words())
