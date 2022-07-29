Total = 0
for i in range(5):
    A = int(input())
    if A < 41 :
        A = 40
    Total += A
print(int(Total/5))