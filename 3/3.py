#!/usr/local/bin/python3

import sys
import re

def check_adj(data,linenum,num,index):
    adjcells = ''
    #check all 8 directions around the num
    #watch boundaries of array
    #linenum must be > 0 and < len(data)
    #data[linenum][index] > 0 and < len(data[linenum])
    ei = index+len(num)-1
    #print("num: ",num," i: ",index," l(n): ",len(num)," ln: ",linenum," ei#: ",data[linenum][ei])
    if (index>0) and (ei+1<len(data[linenum])) and (linenum>0) and (linenum+1<len(data)):
        #bulk of board, check all 8 directions / not on edge
        adjcells = data[linenum-1][index-1:ei+2] + " " + data[linenum+1][index-1:ei+2] + " " + data[linenum][index-1] + " " + data[linenum][ei+1]
        #print(data[linenum-1][index-1:ei+2])
    elif linenum == 0:
        #top row, check below/sides
        #print("linenum=0")
        if index == 0:
            #print("ei+1: ",ei+1,data[linenum+1][ei+1]," wtf: ",index,ei+1)
            adjcells = data[linenum+1][index:ei+2] + " " + data[linenum][ei+1]
            #print("top/0")
        elif ei == len(data[linenum]):
            adjcells = data[linenum+1][index-1:ei] + " " + data[linenum][index-1]
            #print("top/end")
        else:
            #print("top/mid")
            adjcells = data[linenum][index-1] + " " + data[linenum+1][index-1:ei+2] + " " + data[linenum][ei+1]
    elif linenum == (len(data)-1):
        #bottom row, check above/sides
        #print("linenum=len(data)")
        if index == 0:
            adjcells = data[linenum-1][index:ei+2] + " " + data[linenum][ei+1]
        elif ei == len(data[linenum]):
            adjcells = data[linenum-1][index:ei] + " " + data[linenum][index-1]
        else:
            adjcells = data[linenum-1][index-1:ei+2] + " " + data[linenum][index-1] + " " + data[linenum][ei+1]
    elif ei+1 == len(data[linenum]):
        #right edge, check above/below/left side
        #print("index=len(data[linenum])")
        #print("here")
        adjcells = data[linenum-1][index-1:ei] + " " + data[linenum+1][index-1:ei] + " " + data[linenum][index-1]
    elif index == 0:
        #left edge, check above/below/right side
        #print("index=0")
        adjcells = data[linenum-1][index:ei+2] + " " + data[linenum+1][index:ei+1] + " " + data[linenum][ei+1]
    else:
        print("something wrong")

    #print("re.findall result: ",re.findall(r'[^.0-9\s]',adjcells))
    #return bool(re.search(r'[^\.0-9\s]',adjcells))
    valid = bool(re.search(r'[^\.\d\s]',adjcells))
    #print("adjcells: ",adjcells,"valid: ",valid," ln:",linenum," num:",data[linenum][index:ei+1])
    return valid

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
        flag = True
        for num in numlist:
            #then check around that number
            #what about two numbers adjacent but otherwise surrounded by "." ?
            # assuming that both of these numbers would not count as no "symbol"
            # ......
            # .34...
            # ..65..
            # ......

            #if a symbol adjacent somewhere, add to total
            if flag:
                index = data[linenum].find(num)
                flag = False
            else:
                index = data[linenum].find(num,index + len(num) - 1)
            if check_adj(data,linenum,num,index):
                total += int(num)
            #    print("good num: ",num)
            #else:
            #    print("bad num: ",num,linenum)

    print("Total:")
    print(total)

    return

if __name__ == '__main__':
    main()
