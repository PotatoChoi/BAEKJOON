B1 = input()
B2 = input()

B1N = 0
B2N = 0
for i in range(len(B1)) :
    B1N += int(B1[::-1][i]) * (2 ** i)
for i in range(len(B2)) :
    B2N += int(B2[::-1][i]) * (2 ** i)

B3N = B1N * B2N
B3 = ''
while True :
    B3 += str(B3N % 2)
    B3N = B3N // 2
    if B3N == 0 :
        break

print(B3[::-1])