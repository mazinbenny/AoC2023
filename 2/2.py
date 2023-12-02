#!/usr/local/bin/python3

import sys
import re

def main():

    progName = "Day2"

    #which games possible with 12 red, 13 green, 14 blue

    valid_total = 0

    for line in sys.stdin:
        gamelist = line.strip().split(':')
        gamelist[0] = int(re.sub(r'Game ([0-9]+)',r'\1',gamelist[0]))
        gamelist[1] = gamelist[1].split(';')
        for check in range(len(gamelist[1])):
            #if match blue, blue count, else 0
            if re.search('.*[0-9]+ blue.*',gamelist[1][check]):
                blue = int(re.sub(r'.*([0-9]+) blue.*',r'\1',gamelist[1][check]))
            else:
                blue = 0
            print(gamelist[1][check]," ###BLUE: ",blue)

    return

if __name__ == '__main__':
    main()
