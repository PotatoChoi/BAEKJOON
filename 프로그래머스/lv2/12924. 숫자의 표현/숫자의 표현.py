def solution(n):
    answer = 0
    
    for i in range(1, n + 1) :
        board = 0
        for j in range(i, n + 1) :
            board += j
            if board == n :
                answer += 1
                break
            elif board > n :
                break
    
    return answer