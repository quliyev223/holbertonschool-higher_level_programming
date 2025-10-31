#!/usr/bin/python3
if __name__ == "__main__":
    import sys
if len(sys.argv) > 2:
    a = "arguments"
    b = ":"
elif len(sys.argv) == 2:
    a = "argument"
    b = ":"
if len(sys.argv) == 1:
    b = "."
print("{} {}:".format(len(sys.argv) - 1, a))

for i in range(1, len(sys.argv)):
    print("{}: {}".format(i, sys.argv[i]))
