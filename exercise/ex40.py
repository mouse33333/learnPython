#! usr/bin/env Python
# coding=utf-8

cities = {"CA":"San Fancisco", "MI":"Detroit", "FL":"Jacksonville"}

cities["NY"] = "New York"
cities["OR"] = "Portland"

def find_city(themap, state):
    if state in themap:
        return themap[state]
    else:
        return "Not found."

cities["_find"] = find_city

print cities["_find"]

while True:
    print "State? (Enter to quit)",
    state = raw_input("> ")

    if not state: break
    city_found = cities["_find"](cities, state)
    print city_found
