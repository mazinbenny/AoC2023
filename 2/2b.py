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
        maxblue = 0
        maxred = 0
        maxgreen = 0
        for check in range(len(gamelist[1])):
            if re.search('.*[, ][0-9]+ blue.*',gamelist[1][check]):
                blue = int(re.sub(r'.*[, ]([0-9]+) blue.*',r'\1',gamelist[1][check]))
                if blue > maxblue: maxblue = blue
            else:
                blue = 0
            if re.search('.*[, ][0-9]+ red.*',gamelist[1][check]):
                red = int(re.sub(r'.*[, ]([0-9]+) red.*',r'\1',gamelist[1][check]))
                if red > maxred: maxred = red
            else:
                red = 0
            if re.search('.*[, ][0-9]+ green.*',gamelist[1][check]):
                green = int(re.sub(r'.*[, ]([0-9]+) green.*',r'\1',gamelist[1][check]))
                if green > maxgreen: maxgreen = green
            else:
                green = 0

        #after inner loop
        #collect max for each color to mult to power
        power = maxblue * maxred * maxgreen
        print("mb: ",maxblue," mr: ",maxred," mg: ",maxgreen," pwr: ",power)

        valid_total += power


    print("Total of valid game powers:")
    print(valid_total)

    return

if __name__ == '__main__':
    main()
