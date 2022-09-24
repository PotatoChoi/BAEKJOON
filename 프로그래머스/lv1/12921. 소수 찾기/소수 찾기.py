def solution(n):
    answer = 0
    vali = [1] * (n + 1)
    vali[0], vali[1] = 0, 0
    for i in range(2, int(n ** 0.5) + 1) :
        if vali[i] :
            j = 2
            while i * j <= n :
                vali[i*j] = 0
                j += 1
    answer = vali.count(1)
    return answer
