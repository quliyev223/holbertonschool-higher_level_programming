#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str[45:76] + str[98:104]
str = str + str[0:6]
print(str)
