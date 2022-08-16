Word = input()

for i in Word:
    if 65 <= ord(i) <= 90:
        print(chr(ord(i)+32),end='')
    else:
        print(chr(ord(i)-32),end='')