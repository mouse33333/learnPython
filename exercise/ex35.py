#! usr/bin/env Python
# coding=utf-8
from sys import exit

def start():
    print "现在你来到了一个房间，左右各有一扇门，你想选哪个？"
    next = raw_input("请输入你的选择：")
    if "左" in next:
        bear_room()
    elif "右" in next:
        cthulu_room()
    else:
        print "你离开了游戏"
        yes_no = raw_input("想要重新开始吗？是/否: ")
        if "是" in yes_no:
            start()
        else:
            print "再见"

def bear_room():
    print "你看到一只大熊在房间里，身后有一扇门，而房间的另一侧有蜂蜜，你怎么做？"
    print "1: 拿蜂蜜引开熊"
    print "2: 嘲笑它"
    while True:
        next = raw_input("请输入你的选择：")
        if next == "1":
            print "大熊盯着你，然后一巴掌把你拍死了"
        elif next == "2":
            print "熊走开了，现在你可以打开门了"
        elif next == "打开门":
            gold_room()
        else:
            print "请输入数字1或2"


def gold_room():
    print "房间里都是金子，你要拿多少？"
    next = raw_input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("输入错误，你死了")
    if how_much < 50:
        print "你赢了"
        exit(0)
    else:
        dead("你太贪心了")

def cthulu_room():
    print "你看到了一个恶魔，他盯着你，然后你发疯了"
    print "1. 逃跑"
    print "2. 求饶"
    next = raw_input("请输入你的选择：")
    if next == "1":
        start()
    elif next == "2":
        print "恶魔一口把你吃掉了"
        dead("真好吃")
    else:
        cthulu_room()

def dead(why):
    print why, "干得好！"
    exit(0)

start()


