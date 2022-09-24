def solution(numbers):
    answer = set()
    for j in range(len(numbers)) :
        for k in range(len(numbers)) :
            if j != k :
                answer.add(numbers[j] + numbers[k])
    answer = list(answer)
    answer.sort()
    return answer