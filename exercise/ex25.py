#! usr/bin/env Python
# coding=utf-8

import ex24

sentence = "All good things come to those who wait."
words = ex24.break_words(sentence)
print words

sorted_words = ex24.sorted_words(words)
print sorted_words

ex24.print_first_word(words)
ex24.print_last_word(words)
print words

ex24.print_first_word(sorted_words)
ex24.print_last_word(sorted_words)
print sorted_words

sorted_words = ex24.sorted_sentence(sentence)
print sorted_words

ex24.print_first_and_last(sentence)
ex24.print_first_and_last_sorted(sentence)
