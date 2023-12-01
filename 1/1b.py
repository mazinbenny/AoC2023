#!/usr/local/bin/python3

import sys

def main():

    progName = "Day1b"
    total = 0

    for line in sys.stdin:
        #print(line.strip())

        word = ''
        for char in line:
            if char.isdigit():
                #don't need to look for number-word, have a digit
                left = int(char)
                break
            else:
                word += char

            if word.find("one") != -1:
                left = 1
                break
            elif word.find("two") != -1:
                left = 2
                break
            elif word.find("three") != -1:
                left = 3
                break
            elif word.find("four") != -1:
                left = 4
                break
            elif word.find("five") != -1:
                left = 5
                break
            elif word.find("six") != -1:
                left = 6
                break
            elif word.find("seven") != -1:
                left = 7
                break
            elif word.find("eight") != -1:
                left = 8
                break
            elif word.find("nine") != -1:
                left = 9
                break

        word = ''

        for char in reversed(line):
            if char.isdigit():
                right = int(char)
                break
            else:
                #prepend / build the word backwards because of the reverse loop
                word = char + word
            if word.find("one") != -1:
                right = 1
                break
            elif word.find("two") != -1:
                right = 2
                break
            elif word.find("three") != -1:
                right = 3
                break
            elif word.find("four") != -1:
                right = 4
                break
            elif word.find("five") != -1:
                right = 5
                break
            elif word.find("six") != -1:
                right = 6
                break
            elif word.find("seven") != -1:
                right = 7
                break
            elif word.find("eight") != -1:
                right = 8
                break
            elif word.find("nine") != -1:
                right = 9
                break

        total += int(str(left) + str(right))

    print("Total:")
    print(total)

    return

if __name__ == '__main__':
    main()
