#!/usr/bin/python3

from art import text2art

print(text2art("Caesar cipher decoder"))
# inputString = input("Input string")
# inputShift = int(input("Offset/Key (number)"))
inputString = "rovvy ofobilyni"
inputShift = 10
letters = []

for j in inputString:
    letters.append(j)

for i in range(len(letters)):
    kek = ord(letters[i])-inputShift
    print(chr(kek), end="")

if __name__ == '__main__':
    pass


