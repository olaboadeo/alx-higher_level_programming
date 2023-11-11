#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    no = len(sys.argv) - 1

    if no == 0:
        print("{} arguments.".format(no))
    elif no == 1:
        print("{} argument:".format(no))
    else:
        print("{} arguments:".format(no))

    if no >= 1:
        i = 0
        for argu in sys.argv:
            if i != 0:
                print("{}: {}".format(i, argu))
            i += 1
