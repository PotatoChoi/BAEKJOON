num = int(input())

for _ in range(num) :
    N, M = map(int, input().split())
    case = list(map(int, input().split()))
    board = [1] * N
    board[M] = 0
    count = 0
    
    while 1 :
        if max(case) == case[0] :
            count += 1
            if board[0] == 0 :
                print(count)
                break
            else :
                case.pop(0)
                board.pop(0)
        else :
            case.append(case.pop(0))
            board.append(board.pop(0))