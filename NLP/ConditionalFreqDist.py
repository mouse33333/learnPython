#! usr/bin/env Python
# coding = utf-8

from nltk.corpus import brown
import nltk

days = ['Monday', "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

genre_word = [(genre, word)
              for genre in ["news", "romance"]
              for word in brown.words(categories=genre)]

cfd = nltk.ConditionalFreqDist(genre_word)
cfd.tabulate(conditions=["news", "romance"], samples=days)
cfd.plot(conditions=["news", "romance"], samples=days)
