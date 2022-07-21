N=int(input())
M,i = 1,0
while 1:
    i+=1
    if (N-M)>0:
        M+=6*i
    else:
        break
print(i)