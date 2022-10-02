userList = list(map(int, input().split()))
userList.sort()
print(abs((userList[0] + userList[3]) - (userList[1] + userList[2])))