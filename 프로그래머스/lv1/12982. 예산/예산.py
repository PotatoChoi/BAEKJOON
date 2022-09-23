def solution(d, budget):
    answer = 0
    count = 0
    d.sort()
    for i in d :
        budget = budget - i
        if budget >= 0 :
            count += 1
    answer = count
    return answer