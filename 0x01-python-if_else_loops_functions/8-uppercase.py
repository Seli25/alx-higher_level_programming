#!/usr/bin/python3
def uppercase(str):
    while str[i:]:
        ch = ord(str[i])
        if ch >= ord('a') and ch <= ord('z'):
            ch2 += chr(ch-32)
        else:
            ch2 += chr(ch)
        i += 1
    print(ch2)
