N = int(input())

Square = 2

while 1 :
    if (N == 1) or (N == 2) :
        print(N)
        break
    Square *= 2
    if (Square >= N) :
        print((N - (Square // 2)) * 2)
        break