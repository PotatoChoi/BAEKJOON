def solution(answers):
    answer = []
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    
    board = [0,0,0]
    
    for i in range(len(answers)) :
        if answers[i] == one[i % len(one)] :
            board[0] += 1
        if answers[i] == two[i % len(two)] :
            board[1] += 1
        if answers[i] == three[i % len(three)] :
            board[2] += 1
    
    for j in range(board.count(max(board))) :
        answer.append(board.index(max(board)) + 1)
        board[board.index(max(board))] = -1
        
    return answer