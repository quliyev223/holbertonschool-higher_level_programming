#!/usr/bin/python3
import sys
if len(sys.argv) > 1:
    a = "arguments"
    b = ":"
elif len(sys.argv) == 1:
    a = "argument"
    b = ":"
if len(sys.argv) == 0:
    b = "."
print("{} {} {}".format(len(sys.argv), a, b))

for i in range(1, len(sys.argv)):
    print("{}{} {}".format(i, b, sys.argv[i]))
