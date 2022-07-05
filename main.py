#!/usr/bin/python3

from art import text2art
import string

def engBruteforceDecrypt(enc_string):
    LettersAndDigits = string.ascii_letters + string.digits + string.punctuation #lowercase and uppercase eng aphabet + spec. symbols
    print("ROT RIGHT") # Shift right(exp. +i shifts)
    for shift in range(len(enc_string)):
        encoded = ""
        for i in enc_string:
            if i in LettersAndDigits:
                pos = LettersAndDigits.find(i)
                pos -= shift
                if pos < 0:
                    pos += len(LettersAndDigits)
                encoded += LettersAndDigits[pos]
            else:
                encoded += i
        print(f"Shift {shift}: {encoded}")

    print("ROT LEFT")# Shift left(exp. -i shifts)
    for shift in range(len(enc_string)):
        encoded = ""
        for i in enc_string:
            if i in LettersAndDigits:
                pos = LettersAndDigits.find(i)
                pos += shift
                if pos < 0:
                    pos -= len(LettersAndDigits)
                encoded += LettersAndDigits[pos]
            else:
                encoded -= i
        print(f"Shift {shift}: {encoded}")


def rusBruteforceDecrypt(enc_string):
    LettersAndDigits = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ" # russian alphabet
    print("ROT RIGHT")
    for shift in range(len(enc_string)):
        encoded = ""
        for i in enc_string:
            if i in LettersAndDigits:
                pos = LettersAndDigits.find(i)
                pos -= shift
                if pos < 0:
                    pos += len(LettersAndDigits)
                encoded += LettersAndDigits[pos]
            else:
                encoded += i
        print(f"Shift {shift}: {encoded}")
    print("ROT LEFT")
    for shift in range(len(enc_string)):
        encoded = ""
        for i in enc_string:
            if i in LettersAndDigits:
                pos = LettersAndDigits.find(i)
                pos += shift
                if pos < 0:
                    pos -= len(LettersAndDigits)
                encoded += LettersAndDigits[pos]
            else:
                encoded -= i
        print(f"Shift {shift}: {encoded}")

if __name__ == '__main__':
    print(text2art("Caesar cipher decoder"))
    inputLang = input("RUS(1) or ENG(2) string: ")
    inputString = input("Input string: ")
    if inputLang in ("1" or "rus" or "RUS"):
        rusBruteforceDecrypt(inputString)
    else:
        engBruteforceDecrypt(inputString)
