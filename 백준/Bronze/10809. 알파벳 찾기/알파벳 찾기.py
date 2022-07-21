S = input()
for i in range(97,123):
    M=chr(i)
    if M in S:
        print(S.find(M))
    else:
        print("-1")