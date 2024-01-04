#!/usr/bin/python3

if __name__ == "__main__":
    """print result of the addition of all arguments"""

    import sys
    total = 0;
    num = (len(sys.argv) - 1)

    for i in range(num):
        total += int(sys.argv[i + 1])
    print("{}".format(total))
