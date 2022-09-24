def solution(N, stages):
    answer = []
    table = dict()
    user = len(stages)
    
    for i in range(1, N+1):
        if user != 0 :
            table[i] = stages.count(i) / user
            user -= stages.count(i)
        else :
            table[i] = 0
    answer = sorted(table, key = lambda x : table[x], reverse = True)
    return answer