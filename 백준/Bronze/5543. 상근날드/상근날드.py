board = []
for i in range(5):
    board.append(int(input()))
    
print((min(board[0], board[1], board[2]) + min(board[3], board[4])) - 50)
