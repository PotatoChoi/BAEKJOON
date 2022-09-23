def solution(n):
    answer = 0
    result = ''
    while n > 0 :
        n, m = n // 3, n % 3
        result += str(m)
    result = result[::-1]
    for i in range(len(result)) :
        answer += int(result[i]) * 3**i
    return answer