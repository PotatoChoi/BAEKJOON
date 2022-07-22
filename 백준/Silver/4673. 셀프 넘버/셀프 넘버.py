def d(n):
    n = n + sum(map(int, str(n)))
    return n

SelfX = set([])
for i in range(1, 10001):
    SelfX.add(d(i))

for j in range(1, 10001):
    if j not in SelfX:
        print(j)