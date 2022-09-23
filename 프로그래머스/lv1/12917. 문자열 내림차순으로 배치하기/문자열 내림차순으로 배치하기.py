def solution(s):
    answer = ''
    slist = sorted(s, key=ord)
    for i in slist[::-1] :
        answer += i
        
    return answer