while True:
    N = input()
    if N=="0":
        break
    for i in range(len(N)//2+len(N)%2):
        if N[i] == N[-(i+1)]:
            b=1
        else:
            b=0
            break
    if b==1:
        print("yes")
    else:
        print("no")
