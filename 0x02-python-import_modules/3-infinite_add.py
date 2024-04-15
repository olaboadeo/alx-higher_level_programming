#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i, add = 0, 0
    for arg in sys.argv:
        if i != 0:
            no = int(arg)
            add += no
        i += 1

    print(add)
