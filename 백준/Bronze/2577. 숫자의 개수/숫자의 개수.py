A,B,C = [int(input()) for i in range(3)]
D=str(A*B*C)
[print(D.count(f"{i}")) for i in range(10)]