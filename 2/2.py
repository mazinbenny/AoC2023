#!/usr/local/bin/python3

import sys
import re

def main():

    progName = "Day2"

    #which games possible with 12 red, 13 green, 14 blue
    for line in sys.stdin:
        gamelist = line.strip().split(':')
        gamelist[0] = int(re.sub(r'Game ([0-9]+)',r'\1',gamelist[0]))
        gamelist[1] = gamelist[1].split(';')
        print(gamelist)
        print(len(gamelist[1]))

    return

if __name__ == '__main__':
    main()
