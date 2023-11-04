#!/usr/bin/python3
for first_dig in range(0, 10):
    for last_dig in range(first_dig + 1, 10):
        print("{:d}{:d}".format(first_dig, last_dig),
              end='\n' if first_dig == 8 and last_dig == 9 else ", ")
