#! usr/bin/env Python
# coding=utf-8

from sys import argv

script, user_name = argv

prompt = "> "

print "Hi %s, I'm the %s script." %(user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
live = raw_input(prompt)

print "What kind of computer do you like %s?" % user_name
computer = raw_input(prompt)

print '''
So you said %r about liking me.
You live in %r. Don't know where it is.
And you've a %r computer. Nice
'''% (likes, live, computer)
