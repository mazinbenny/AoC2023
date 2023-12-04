#!/usr/local/bin/python3

import sys
import re

def main():

    progName = "Day4"
    total = 0

    data = []
    for line in sys.stdin:
        data.append(line.strip())

    for linenum in range(len(data)):
        nolabel = re.sub(r'Card\s+\d+: ','',data[linenum])
        nums = nolabel.split('|')
        win = set(re.findall(r'\d+',nums[0]))
        mine = set(re.findall(r'\d+',nums[1]))
        if len(mine.intersection(win)) > 0:
            total += 2**(len(mine.intersection(win)) - 1)

    print("Total:")
    print(total)

    return

if __name__ == '__main__':
    main()
