def solution(dartResult):
    answer = 0
    bonus = [0, 'S', 'D', 'T']
    board = []
    num = ''
    
    for i in dartResult :
        if i.isdigit() :
            num += i
        else :
            if i.isalpha() :
                board.append(int(num))
                board[-1] = board[-1] ** (bonus.index(i))
                num = ''
            if i.isalpha() is not True :
                if i == '*' :
                    if len(board) == 1 :
                        board[-1] *= 2
                    else :
                        board[-1] *= 2
                        board[-2] *= 2
                else :
                    board[-1] = -(board[-1])
        print(board)
        answer = sum(board)
    return answer