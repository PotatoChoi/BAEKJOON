def solution(nums):
    answer = 0
    vali = [1] * (max(nums) * 3 + 1)
    vali[0], vali[1] = 0, 0
    
    board = []
    
    for i in range(2, int((max(nums) * 3) ** 0.5) + 1) :
        if vali[i] :
            j = 2
            while i * j <= max(nums) * 3 :
                vali[i * j] = 0
                j += 1
    
    
    for i in nums :
        for j in nums :
            for k in nums :
                if i != j and i != k and j != k :
                    if vali[i + j + k] == 1 :
                        if sorted([i,j,k]) not in board :
                            board.append(sorted([i,j,k]))
    
    answer = len(board)

    return answer