while True:
    N = input()
    if N=="0":
        break
    for i in range(len(N)//2+len(N)%2):
        if N[i] == N[-(i+1)]:
            b="yes"
        else:
            b="no"
            break
    print(b)
