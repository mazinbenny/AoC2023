#!/usr/local/bin/python3

import sys
import re

def main():

    progName = "Day3"
    total = 0

    data = []
    for line in sys.stdin:
        data.append(line.strip())

    #walk through each line
    #search for numbers, check adjacent spaces (with array limits checked)
    #if all "." around the number, ignore, anything else, add number to total
    for linenum in range(len(data)):
        #re seach? findall? for nums in the data[linenum]
            #subloop through each number on the line
            #then check around that number
            #what about two numbers adjacent but otherwise surrounded by "." ?
            # ......
            # .34...
            # ..65..
            # ......
            #if a symbol adjacent somewhere, add to total

    print("Total:")
    print(total)

    return

if __name__ == '__main__':
    main()
