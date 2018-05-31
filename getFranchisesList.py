#!/usr/bin/python3.6
# -*-coding:Utf-8 -*

import sys

path = "data/Wikipedia - Video Games Franchise List.txt"
file = open(path, "r")
fileContent = str(file.read())
file.close()

lines = fileContent.split("\n")

i = 0

for l in lines:
    franchise = ""
    if not (l[0:1] == "#" and i == 0):
        check = False

        check = l.find("[")

        if check > 0:
            franchise = l[0:check]
        else:
            franchise = l
    print(franchise)
    i+=1
