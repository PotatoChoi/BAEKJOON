def solution(s):
    answer = [0, 0]
    while s != '1' :
        answer[1] += s.count('0')
        s = s.replace('0', '')
        
        rebi = ''
        s = len(s)
        while 1 :
            if s // 2 != 0 :
                rebi += str(s % 2)
                s = s // 2
            else :
                rebi += str(s)
                s = rebi[::-1]
                break
                
        answer[0] += 1
        
    return answer