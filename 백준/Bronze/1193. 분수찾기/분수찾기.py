X=int(input())
i=1
while X>i:
    X-=i
    i+=1
if i%2==0:
    A=X
    B=i-X+1
else:
    A=i-X+1
    B=X
print(f"{A}/{B}")