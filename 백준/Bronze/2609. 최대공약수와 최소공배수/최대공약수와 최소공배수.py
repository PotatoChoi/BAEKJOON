A, B = map(int, input().split())
def Gcd(A, B):
    while B:
        A, B = B, A%B
    return A

print(Gcd(A,B))
print(A*B//Gcd(A,B))