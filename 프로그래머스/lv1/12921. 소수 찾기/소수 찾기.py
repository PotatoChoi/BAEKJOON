def solution(n):
    answer = 0
    vali = [True] * (n + 1)
    vali[0], vali[1] = False, False
    for i in range(2, int(n ** 0.5) + 1) :
        if vali[i] :
            j = 2
            while i * j <= n :
                vali[i*j] = False
                j += 1
    answer = vali.count(True)
    return answer