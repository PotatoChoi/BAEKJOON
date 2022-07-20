A,B,C = input().split()
A,B,C = int(A),int(B),int(C)
D=int(0)
AList=[A,B,C]
AList.sort()
if A==B:
    D+=1
if A==C:
    D+=1
if B==C:
    D+=1
if D==0:
    print(AList[2]*100)
elif D==1:
    if (AList[0]==AList[1]) | (AList[0]==AList[2]):
        print((AList[0]*100)+1000)
    else:
        print((AList[1]*100)+1000)
else:
    print((A*1000)+10000)