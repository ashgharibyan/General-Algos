#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    isPM = (s[8:10] == "PM")
    hh = int(s[0:2])
    if isPM:
        if  hh < 12:
            hh += 12
    else:
        print("Im here")
        if hh == 12:
            hh -= 12
    
    return str(hh) + s[2:8]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
