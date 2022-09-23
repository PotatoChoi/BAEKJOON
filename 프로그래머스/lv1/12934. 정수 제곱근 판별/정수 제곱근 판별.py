def solution(n):
    answer = 0
    square = n ** 0.5
    if square == int(square) :
        answer = (square+1) ** 2
    else :
        answer = -1
    return answer