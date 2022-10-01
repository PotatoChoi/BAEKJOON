N = input()

A, B = '', ''
for i in range(len(N)) :
    if i == 0 or (i == 1 and N[i] == '0') :
        A += N[i]
    else :
        B += N[i]

print(int(A) + int(B))