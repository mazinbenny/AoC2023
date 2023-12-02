#!/usr/local/bin/python3

import sys
import re

def main():

    progName = "Day2"

    valid_total = 0

    for line in sys.stdin:
        gamelist = line.strip().split(':')
        gamelist[0] = int(re.sub(r'Game ([0-9]+)',r'\1',gamelist[0]))
        gamelist[1] = gamelist[1].split(';')
        valid = True
        for check in range(len(gamelist[1])):
            #if match blue, blue count, else 0
            if re.search('.*[, ][0-9]+ blue.*',gamelist[1][check]):
                blue = int(re.sub(r'.*[, ]([0-9]+) blue.*',r'\1',gamelist[1][check]))
            else:
                blue = 0
            if re.search('.*[, ][0-9]+ red.*',gamelist[1][check]):
                red = int(re.sub(r'.*[, ]([0-9]+) red.*',r'\1',gamelist[1][check]))
            else:
                red = 0
            if re.search('.*[, ][0-9]+ green.*',gamelist[1][check]):
                green = int(re.sub(r'.*[, ]([0-9]+) green.*',r'\1',gamelist[1][check]))
            else:
                green = 0

            #which games possible with 12 red, 13 green, 14 blue
            #print("red: ",red," green: ",green," blue: ",blue)
            if red > 12 or green > 13 or blue > 14:
                valid = False
                break
        #after inner loop
        if valid:
            #print(gamelist)
            valid_total += gamelist[0]


    print("Total of valid game IDs:")
    print(valid_total)

    return

if __name__ == '__main__':
    main()
