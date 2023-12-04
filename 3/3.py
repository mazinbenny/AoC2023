#!/usr/local/bin/python3

import sys
import re

def check_adj(data,linenum,num):
    index = data[linenum].find(num)
    adjcells = ''
    #check all 8 directions around the num
    #watch boundaries of array
    #linenum must be > 0 and < len(data)
    #data[linenum][index] > 0 and < len(data[linenum])
    print("num: ",num," i: ",index," l(n): ",len(num)," ln: ",linenum," l(ln): ",len(data[linenum]))
    if (index>0) and (index+len(num)+1 <= len(data[linenum])) and (linenum>0) and (linenum+1 <= len(data)):
        #bulk of board, check all 8 directions / not on edge
        #if re.search(r'^[.\d\l]',data[linenum][index-1:index+len(num)+1]):
        adjcells = data[linenum-1][index-1:index+len(num)+1] + data[linenum+1][index-1:index+len(num)+1] + data[linenum][index-1] + data[linenum][index+len(num)+1]
        print("main board")
    elif linenum == 0:
        #top row, check below/sides
        print("linenum=0")
        if index == 0:
            adjcells = data[linenum+1][index:index+len(num)+1] + data[linenum][index+len(num)+1]
        elif index+len(num) == len(data[linenum]):
            adjcells = data[linenum][index-1] + data[linenum+1][index-1:index+len(num)]
        else:
            adjcells = data[linenum][index-1] + data[linenum+1][index-1:index+len(num)+1] + data[linenum][index+len(num)+1]
    elif linenum == len(data):
        #bottom row, check above/sides
        print("linenum=len(data)")
        if index == 0:
            adjcells = data[linenum-1][index:index+len(num)+1] + data[linenum][index+len(num)+1]
        elif index+len(num) == len(data[linenum]):
            adjcells = data[linenum-1][index:index+len(num)] + data[linenum][index-1]
        else:
            adjcells = data[linenum-1][index-1:index+len(num)+1] + data[linenum][index-1] + data[linenum][index+len(num)+1]
    elif index+len(num) == len(data[linenum]):
        #right edge, check above/below/left side
        print("index=len(data[linenum])")
        adjcells = data[linenum-1][index-1:index+len(num)] + data[linenum][index-1] + data[linenum+1][index-1:index+len(num)]
    elif index == 0:
        #left edge, check above/below/right side
        print("index=0")
        adjcells = data[linenum-1][index:index+len(num)+1] + data[linenum][index+len(num)+1] + data[linenum+1][index:index+len(num)+1]
    else:
        print("something wrong")

    print("adjcells: ",adjcells)
    print("re.findall result: ",re.findall(r'[^.0-9]',adjcells))
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
        #print("line: ",data[linenum])
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
                print("good num: ",num)
            else:
                print("bad num: ",num)

    print("Total:")
    print(total)

    return

if __name__ == '__main__':
    main()
