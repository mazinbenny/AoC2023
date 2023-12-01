#!/usr/local/bin/python3

import sys

def main():

    progName = "Day1"
    total = 0

    line_pos = [100] * 10
    line_Rpos = [-1] * 10

    for line in sys.stdin:
        line.strip()

        print(line)

        lowest = len(line) - 1
        highest = 0

        #line = str("0").join(line.split("zero",1))
        #this didn't work because of the "eightwo123" type case... I need 8, but it swapped 2 first

        line_pos[0] = line.index("zero")  if "zero"  in line else len(line) #4c
        line_pos[1] = line.index("one")   if "one"   in line else len(line) #3c
        line_pos[2] = line.index("two")   if "two"   in line else len(line) #3c
        line_pos[3] = line.index("three") if "three" in line else len(line) #5c
        line_pos[4] = line.index("four")  if "four"  in line else len(line) #4c
        line_pos[5] = line.index("five")  if "five"  in line else len(line) #4c
        line_pos[6] = line.index("six")   if "six"   in line else len(line) #3c
        line_pos[7] = line.index("seven") if "seven" in line else len(line) #5c
        line_pos[8] = line.index("eight") if "eight" in line else len(line) #5c
        line_pos[9] = line.index("nine")  if "nine"  in line else len(line) #4c

        line_Rpos[0] = line.rindex("zero")  if "zero"  in line else -1
        line_Rpos[1] = line.rindex("one")   if "one"   in line else -1
        line_Rpos[2] = line.rindex("two")   if "two"   in line else -1
        line_Rpos[3] = line.rindex("three") if "three" in line else -1
        line_Rpos[4] = line.rindex("four")  if "four"  in line else -1
        line_Rpos[5] = line.rindex("five")  if "five"  in line else -1
        line_Rpos[6] = line.rindex("six")   if "six"   in line else -1
        line_Rpos[7] = line.rindex("seven") if "seven" in line else -1
        line_Rpos[8] = line.rindex("eight") if "eight" in line else -1
        line_Rpos[9] = line.rindex("nine")  if "nine"  in line else -1

        for loop in range(9):
            if line_pos[loop] < lowest:
                lowest = line_pos[loop]
            if line_Rpos[loop] > highest:
                highest = line_pos[loop]

        print("lowest is: ", lowest)
        print("high   is: ", highest)


        print(line)

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
