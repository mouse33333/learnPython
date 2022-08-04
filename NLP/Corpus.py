#! usr/bin/env Python
# coding = utf-8

from nltk.corpus import gutenberg

print gutenberg.fileids()

for fileid in gutenberg.fileids():
    num_char = len(gutenberg.raw(fileid))
    num_words = len(gutenberg.words(fileid))
    num_sents = len(gutenberg.sents(fileid))
    num_vocab = len(set([w.lower() for w in gutenberg.words(fileid)]))
    print int(num_char/num_words), int(num_words/num_sents), int(num_words/num_vocab), fileid

macbath_sents = gutenberg.sents("shakespeare-macbeth.txt")

print macbath_sents
