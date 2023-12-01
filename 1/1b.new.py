#!/usr/local/bin/python3

import sys

def main():

    progName = "Day1b"
    total = 0

    for line in sys.stdin:
        line.strip()

        print(line)
        low = -1
        high = -1
        #this didn't work because of the "eightwo123" type case... I need 8, but it swapped 2 first
        zero_pos = line.find("zero")
        one_pos = line.find("one")
        two_pos = line.find("two")
        three_pos = line.find("three")
        four_pos = line.find("four")
        five_pos = line.find("five")
        six_pos = line.find("six")
        seven_pos = line.find("seven")
        eight_pos = line.find("eight")
        nine_pos = line.find("nine")
        #only replace the lowest and highest found numbers
        print(line)

        word = ''
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
