#!/usr/bin/python3

import re
import math

file = "log_vertical_room.txt"

f = open(file, 'r')
line = f.readline()
ignore_line = 1

for line in f:
    if ignore_line > 8:
        line = line.strip().rstrip('\n').split(",")
        s = float(line[1])
        c = float(line[2])
        r = s * math.pi/180
        a = c * math.cos(r)
        b = c * math.sin(r)
        print(line[0] + " " + str(a) + " " + str(b)) #  + " " + "1.0")
    else:    
        ignore_line = ignore_line + 1

f.close()
