#!/usr/local/bin/python3

import sys
import re

def main():

    progName = "Day4b"
    total = 0

    data = []
    for line in sys.stdin:
        data.append(line.strip())

    cardcnt = [1] * len(data)
    for linenum in range(len(data)):
        nolabel = re.sub(r'Card\s+\d+: ','',data[linenum])
        nums = nolabel.split('|')
        win = set(re.findall(r'\d+',nums[0]))
        mine = set(re.findall(r'\d+',nums[1]))
        if len(mine.intersection(win)) > 0:
            #total += 2**(len(mine.intersection(win)) - 1)
            #make array of game number and the number of copies
            for oloop in range(cardcnt[linenum]):
                for loop in range(linenum + 1,linenum + 1 + len(mine.intersection(win))):
                    cardcnt[loop] += 1

    for linenum in range(len(data)):
        total += cardcnt[linenum]



    print("Total:")
    print(total)

    return

if __name__ == '__main__':
    main()
