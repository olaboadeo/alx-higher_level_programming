#!/usr/bin/python3
def upper(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return (ord(c) - 32)
    else:
        return ord(c)

def uppercase(str):
    new = ""
    for character in str:
        new += "%c" % upper(character)
    print("{:s}".format(new))
