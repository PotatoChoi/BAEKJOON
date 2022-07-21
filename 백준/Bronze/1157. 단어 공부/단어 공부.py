M = input().lower()
Re = [M.count(chr(i)) for i in range(97,123)]
if Re.count(max(Re))==1:
    print(chr(65+Re.index(max(Re))).upper())
else:
    print("?")