#!/usr/local/bin/python3

import sys

def main():

    progName = "Day1"
    total = 0

    for line in sys.stdin:
        line.strip()

        print(line)

        word = ''
        og_line = line
        for char in og_line:
            if char.isdigit():
                left = int(char)
                break
            else:
                word += char
            #originally tried == but exact match doesn't work for leading chars
            if word.find("one") != -1:
                left = 1
                line = line.replace("one","1")
                break
            elif word.find("two") != -1:
                left = 2
                line = line.replace("two","2")
                break
            elif word.find("three") != -1:
                left = 3
                line = line.replace("three","3")
                break
            elif word.find("four") != -1:
                left = 4
                line = line.replace("four","4")
                break
            elif word.find("five") != -1:
                left = 5
                line = line.replace("five","5")
                break
            elif word.find("six") != -1:
                left = 6
                line = line.replace("six","6")
                break
            elif word.find("seven") != -1:
                left = 7
                line = line.replace("seven","7")
                break
            elif word.find("eight") != -1:
                left = 8
                line = line.replace("eight","8")
                break
            elif word.find("nine") != -1:
                left = 9
                line = line.replace("nine","9")
                break
            elif word.find("zero") != -1:
                left = 0
                line = line.replace("zero","0")
                break

        print(line)
        og_line = line
        word = ''

        for char in reversed(og_line):
            if char.isdigit():
                right = int(char)
                break
            else:
                #build the word backwards
                word = char + word
            print("Word: " + word)
            if word.find("one") != -1:
                right = 1
                line = str(right).join(line.rsplit("one",1))
                break
            elif word.find("two") != -1:
                right = 2
                line = str(right).join(line.rsplit("two",1))
                break
            elif word.find("three") != -1:
                right = 3
                line = str(right).join(line.rsplit("three",1))
                break
            elif word.find("four") != -1:
                right = 4
                line = str(right).join(line.rsplit("four",1))
                break
            elif word.find("five") != -1:
                right = 5
                line = str(right).join(line.rsplit("five",1))
                break
            elif word.find("six") != -1:
                right = 6
                line = str(right).join(line.rsplit("six",1))
                print("new: " + line)
                break
            elif word.find("seven") != -1:
                right = 7
                line = str(right).join(line.rsplit("seven",1))
                break
            elif word.find("eight") != -1:
                right = 8
                line = str(right).join(line.rsplit("eight",1))
                break
            elif word.find("nine") != -1:
                right = 9
                line = str(right).join(line.rsplit("nine",1))
                break
            elif word.find("zero") != -1:
                right = 0
                line = str(right).join(line.rsplit("zero",1))
                break

        print(line)
        print("left: ",left," right: ",right)
        #print("left=" + str(left) + " right=" + str(right) + "\n")
        total += int(str(left) + str(right))

    print("Total:")
    print(total)

    return

if __name__ == '__main__':
    main()
