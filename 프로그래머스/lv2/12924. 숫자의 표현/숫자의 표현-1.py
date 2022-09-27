def solution(n):
    answer = 0
    for i in range(1, n + 1, 2) :
        if n & i == 0 :
            answer += 1

  return answer

# n 이하인 숫자 a 부터 i 개의 연속된 숫자의 합이 n 이라고 가정할 때,
# a + (a+1) + (a+2) + (a+3) + ... + (a+i-1) = k(2a+i-1)/2 = n 이다.
# 이 때 a <= n, i < n, a와 i는 자연수 이다.
# a = n/i + (1-i)/2, a는 자연수여햐 하니까, i는 n의 약수여야 하고, (1-i)/2 가 정수여야 하면, 1-i는 짝수여야 하니 i는 홀수여야 한다.
# n의 약수이면서 홀수인 i 갯수.
