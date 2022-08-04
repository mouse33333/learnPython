# coding:utf-8
import random

guess_times = 0

right_number = random.randint(0, 9)

while guess_times < 4:
    guess_number = raw_input('请输入猜测的数字：')
    guess_times += 1
    left_times = 3 - guess_times
    if not guess_number.isdigit():
        print '请输入纯数字'
    elif int(guess_number) not in range(0, 101):
        print '请输入一个0~100的数字'
    else:
        if int(guess_number) == right_number:
            print "你答对了"
            break
        elif int(guess_number) < right_number:
            print '你猜小了，你还剩余%s次机会' % left_times
        elif int(guess_number) > right_number:
            print '你猜大了，你还剩余%s次机会' % left_times

