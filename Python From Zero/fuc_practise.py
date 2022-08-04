#!/usr/bin/env python
# coding = utf-8

import math

def xx2(a, b, c):
    delta = (b**2 - 4*a*c)
    if delta < 0:
        print "delta is less than zero, please input a b c again."
    if delta == 0:
        x0 = - (b / 2*a)
        print x0
    else:
        x1 = (math.sqrt(delta) - b) / (2*a)
        x2 = (- math.sqrt(delta) - b) / (2*a)
        print x1, x2

xx2(1,3,2)

def score(**kargs):
    sum_score = sum(kargs.values())
    print "the average score is", sum_score/len(kargs)

score(m=100, c=50, haha=100)

def sorted_score(scores):
    score_lst = [(scores[k],k) for k in scores]
    score_sorted = sorted(score_lst,reverse=True)
    return [(i[1], i[0]) for i in score_sorted]

scores = {'abc':78, 'M':99, 'Albert':99, 'Af':34, 'Bef':34}
result = sorted_score(scores)
print result

def max_score(scores):
    score_lst = [(scores[k],k) for k in scores]
    score_sorted = sorted(score_lst, reverse = True)
    max_score_class = score_sorted[0][0]
    return [(i[1], i[0]) for i in score_sorted if i[0] == max_score_class]

scores = {'abc':78, 'M':99, 'Albert':99, 'Af':34, 'Bef':34}
print max_score(scores)
