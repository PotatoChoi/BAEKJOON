def solution(n):
    answer = 0
    testlist = []
    for i in str(n) :
        testlist.append(int(i))
    testlist.sort()
    for i in range(len(testlist)) :
        answer += testlist[i]*(10**i)
    return answer