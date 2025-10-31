#!/usr/bin/python3
if __name__ == "__main__":
    import sys

for i in range(1,(len(sys.argv) - 1)):
    add = 0
    add += sys.argv[i]
print(add)
