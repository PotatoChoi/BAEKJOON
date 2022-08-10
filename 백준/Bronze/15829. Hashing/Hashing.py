L = int(input())
Stable = input()
Result = 0
for i in range(L):
    Result += (ord(Stable[i])-96)*(31**i)

print(Result % 1234567891)