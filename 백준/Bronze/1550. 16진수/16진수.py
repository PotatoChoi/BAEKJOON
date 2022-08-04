Num = list(input())
j=0
Result=0
Num.reverse()
for i in Num:
    ConA = ord(i)
    if 47 < ConA < 58 :
        Result += ((ConA%48)*(16**j))
    else :
        Result += ((ConA%55)*(16**j))
    j+=1
print(Result)