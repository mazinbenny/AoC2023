#!/usr/local/bin/python3
#test

import sys

def main():

    progName = "Day1b"
    total = 0

    for line in sys.stdin:
        #print(line.strip())

        word = ''
        og_line = line
        for char in og_line:
            if char.isdigit():
                break
            word += char
            #originally tried == but exact match doesn't work for leading chars
            if word.find("one") != -1:
                line = line.replace("one","1")
                break
            elif word.find("two") != -1:
                line = line.replace("two","2")
                break
            elif word.find("six") != -1:
                line = line.replace("six","6")
                break
            elif word.find("four") != -1:
                line = line.replace("four","4")
                break
            elif word.find("five") != -1:
                line = line.replace("five","5")
                break
            elif word.find("nine") != -1:
                line = line.replace("nine","9")
                break
            elif word.find("three") != -1:
                line = line.replace("three","3")
                break
            elif word.find("seven") != -1:
                line = line.replace("seven","7")
                break
            elif word.find("eight") != -1:
                line = line.replace("eight","8")
                break

        #print(line)
        og_line = line
        word = ''

        for char in reversed(og_line):
            if char.isdigit():
                break
            #prepend / build the word backwards because of the reverse loop
            word = char + word
            #print("Word: " + word)
            if word.find("one") != -1:
                line = str("1").join(line.rsplit("one",1))
                break
            elif word.find("two") != -1:
                line = str("2").join(line.rsplit("two",1))
                break
            elif word.find("six") != -1:
                line = str("6").join(line.rsplit("six",1))
                break
            elif word.find("four") != -1:
                line = str("4").join(line.rsplit("four",1))
                break
            elif word.find("five") != -1:
                line = str("5").join(line.rsplit("five",1))
                break
            elif word.find("nine") != -1:
                line = str("9").join(line.rsplit("nine",1))
                break
            elif word.find("three") != -1:
                line = str("3").join(line.rsplit("three",1))
                break
            elif word.find("seven") != -1:
                line = str("7").join(line.rsplit("seven",1))
                break
            elif word.find("eight") != -1:
                line = str("8").join(line.rsplit("eight",1))
                break

        #print(line.strip())

        for char in line:
            if char.isdigit():
                left = int(char)
                break
        for char in reversed(line):
            if char.isdigit():
                right = int(char)
                break

        print("left: ",left," right: ",right)
        total += int(str(left) + str(right))

    print("Total:")
    print(total)

    return

if __name__ == '__main__':
    main()
