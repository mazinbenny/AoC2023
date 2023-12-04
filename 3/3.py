#!/usr/local/bin/python3

import sys
import re

def check_adj(data,linenum,num):
    index = data[linenum].find(num)
    #check all 8 directions around the num
    #watch boundaries of array
    #linenum must be > 0 and < len(data)
    #data[linenum][index] > 0 and < len(data[linenum])
    if (index>1) and (index+len(num)+1 < len(data[linenum])) and (linenum>1) and (linenum+1 < len(data)):
        #bulk of board, check all 8 directions / not on edge
        #if re.search(r'^[.\d\l]',data[linenum][index-1:index+len(num)+1]):
        adjcells = data[linenum-1][index-1:index+len(num)+1] + data[linenum+1][index-1:index+len(num)+1] + data[linenum][index-1] + data[linenum][index+len(num)+1]
    elif index == 0:
        #top row, check below/sides
        print("index=0")
    elif linenum == len(data):
        #bottom row, check above/sides
        print("linenum=len(data)")
    elif index == len(data[linenum]):
        #right edge, check above/below/left side
        print("index=len(data[linenum])")
    elif index == 0:
        #left edge, check above/below/right side
        print("index=0")

    return bool(re.search(r'[^.0-9]',adjcells))

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
        #re.findall for nums in the data[linenum]
        numlist = re.findall(r'\d+',data[linenum])
        print("line: ",data[linenum])
        #subloop through each number on the line
        for num in numlist:
            #then check around that number
            #what about two numbers adjacent but otherwise surrounded by "." ?
            # assuming that both of these numbers would not count as no "symbol"
            # ......
            # .34...
            # ..65..
            # ......

            #if a symbol adjacent somewhere, add to total
            if check_adj(data,linenum,num):
                total += int(num)

    print("Total:")
    print(total)

    return

if __name__ == '__main__':
    main()
