#!/usr/local/bin/python3

import sys

def main():

    progName = "Day1"
    total = 0

    for line in sys.stdin:
        line.strip()
        #print(line)
        for char in line:
            if char.isdigit():
                left = int(char)
                break
        for char in reversed(line):
            if char.isdigit():
                right = int(char)
                break

        #print("left=" + str(left) + " right=" + str(right) + "\n")
        total += int(str(left) + str(right))

    print("Total:")
    print(total)

    return

if __name__ == '__main__':
    main()
